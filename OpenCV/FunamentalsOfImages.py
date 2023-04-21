import cv2
import random


img = cv2.imread('D:\Desktop\Python-Programs\spidey.jpg', 1)
# Change first 100 rows to random pixels
for i in range(10):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of image
#tag = img[65:165, 125:225]
#img[100:200, 150:250] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()