import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(frame, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(frame, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_TRIPLEX
    img = cv2.putText(img, 'I am nice',(100, height-20), font, 2, (69, 69, 69), 5, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()