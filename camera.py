import cv2

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
