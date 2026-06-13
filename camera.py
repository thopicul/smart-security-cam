import cv2

# Initlize the Webcam
cap = cv2.VideoCapture(0)

# check if the webcome is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to close the video window.")

while True:
    # Capture frame by frame
    ret, frame = cap.read()
    # if frame is read correctly ret is true
    if not ret:
        print("Can't receive frame. exiting..")
        break
    cv2.imshow("'Macbook webcam Feed", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
