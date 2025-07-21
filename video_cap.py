import cv2

cap = cv2.VideoCapture("input1.mp4")

if not cap.isOpened():
    print("Error", "could not open camera")
    exit()

new_width = 940
new_height = 780

while True: 
    ret, frame = cap.read()

    if not ret:
        break

    #resize frame to new dims 
    smaller_frame = cv2.resize(frame, (new_width, new_height))

    cv2.imshow("image", smaller_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()
