import cv2


img = cv2.imread('D:\Desktop\Python-Programs\spidey.jpg', 1)

#img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Image', img)

cv2.waitKey(0)
#if k == ord("s"):
    #cv2.imwrite("starry_night.png", img)
cv2.destroyAllWindows()