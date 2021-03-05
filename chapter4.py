import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
img[100:250] = 255, 0, 0
cv2.line(img, (0, 0), (img.shape[1], img.shape[1]), (0,255, 0), 3)
cv2.rectangle(img, (50, 50), (250, 350), (0,255, 255), 3)
cv2.circle(img, (140, 380), 55, (123, 123, 321), 3)
cv2.putText(img, "OpenCV", (300, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (50, 250, 100), 1)

cv2.imshow("Img", img)
cv2.waitKey(0)