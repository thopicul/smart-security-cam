import cv2

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


# detecting camera

"""
stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("no camera detected")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

fourcc = cv2.VideoWriter.fourcc("m", "p", "4", "v")
output = cv2.VideoWriter("stream.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = stream.read()
    if not ret:
        print("failed to grab frame")
        break
    output.write(frame)
    cv2.imshow("webcame", frame)
    if cv2.waitKey(1) == ord("q"):
        break
stream.release()
cv2.destroyAllWindows()
"""
