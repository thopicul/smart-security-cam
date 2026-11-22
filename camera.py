import cv2

"""
img = cv2.imread("assets/random.png", cv2.IMREAD_COLOR)

if img is not None:
    print(img.shape)
    # print(img[0, 0])
    # rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(rgb_img[0, 0])
    # for i in range(img.shape[0]):
    #     for j in range(img.shape[1]):
    #         img[i, j] = max(254, img[i, j] * 2)
    cv2.imshow("image", img)  # type: ignore
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("assets/gray.png", gray_img)
else:
    print("image not found")
"""

# detecting camera


def main():
    stream = cv2.VideoCapture("assets/walking.mp4")

    if not stream.isOpened():
        print("no camera detected")
        exit()

    fps = stream.get(cv2.CAP_PROP_FPS)
    width = int(stream.get(3))
    height = int(stream.get(4))

    fourcc = cv2.VideoWriter.fourcc("m", "p", "4", "v")
    output = cv2.VideoWriter("stream.mp4", fourcc, fps, (width, height))

    while True:
        ret, frame1 = stream.read()
        ret, frame2 = stream.read()
        if not ret:
            print("failed to grab frame")
            break
        frame1 = cv2.flip(frame1, 1)
        frame2 = cv2.flip(frame2, 1)
        """
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(frame, (5, 5), 0)
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        blur2 = cv2.GaussianBlur(frame2, (5, 5), 0)
        """

        diff = cv2.absdiff(frame1, frame2)  # finding absolute difference between two
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        # grey scale mode for better performance
        # easier to find the contours in greyscale mode compared to color mode

        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # kernel size is 5,5 and sigma is 0, which means that the kernel size is calculated based on the sigma value
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        # thresholding is used to convert the image into binary image, which means that the pixel values are either 0 or 255
        dilated = cv2.dilate(thresh, None, iterations=3)
        # dilating is used to increase the size of the object in the image, which means that the pixel values are either 0 or 255
        contours, _ = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        # countours are the boundaries of the objects in the image, and they are used to detect the movement of the objects in the image

        for contour in contours:
            # loop through all the contours and find the bounding rectangle for each contour, and then draw the rectangle on the frame1
            x, y, width, height = cv2.boundingRect(contour)

            if cv2.contourArea(contour) < 900:
                # if the area of the contour is less than 700, then it is considered as noise and ignored
                continue
            cv2.rectangle(frame1, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv2.putText(
                frame1,
                "Status: {}".format("Movement"),
                (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3,
            )
        # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        output.write(frame1)
        cv2.imshow("webcam box", frame1)

        if cv2.waitKey(1) == ord("q"):
            break
    output.release()
    stream.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
# test
