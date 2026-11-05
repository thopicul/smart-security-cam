import cv2

# img = cv2.imread("assets/random.png", cv2.IMREAD_COLOR)

# if img is not None:
#     print(img.shape)
#     # print(img[0, 0])
#     # rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     # print(rgb_img[0, 0])
#     # for i in range(img.shape[0]):
#     #     for j in range(img.shape[1]):
#     #         img[i, j] = max(254, img[i, j] * 2)
#     cv2.imshow("image", img)  # type: ignore
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite("assets/gray.png", gray_img)
# else:
#     print("image not found")


# detecting camera


stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("no camera detected")
    exit()

# --- NEW: Load OpenCV's built-in object (face) detector ---
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

fps = stream.get(cv2.CAP_PROP_FPS)
# If your camera returns 0 for FPS, fallback to a standard default like 30.0
if fps == 0 or fps is None:
    fps = 30.0

width = int(stream.get(3))
height = int(stream.get(4))

fourcc = cv2.VideoWriter.fourcc("m", "p", "4", "v")
output = cv2.VideoWriter("stream.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = stream.read()
    if not ret:
        print("failed to grab frame")
        break

    # --- NEW: Process the frame to detect objects ---
    # 1. Convert to grayscale (required by Haar Cascades for speed)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Find the coordinates of faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # 3. Draw rectangles on the live frame over detected objects
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            "Object: Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    # Write the frame (now with bounding boxes) to the video file
    output.write(frame)

    cv2.imshow("webcame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

# Clean up everything properly
stream.release()
output.release()  # Good practice to explicitly release the writer
cv2.destroyAllWindows()
