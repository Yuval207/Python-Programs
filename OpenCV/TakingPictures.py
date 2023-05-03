import cv2

def TakePics():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('webcamPhoto.jpg', frame)
    cap.release()


TakePics()