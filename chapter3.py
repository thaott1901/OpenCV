import cv2
import numpy as np

img = cv2.imread("rsc/salter.jpg")
print(img.shape)

imgResize = cv2.resize(img, (224, 224))
imgCropped = img[400:1000, 100:1000]

cv2.imshow("Img", img)
cv2.imshow("Img Resize", imgResize)
cv2.imshow("Img Cropped", imgCropped)
cv2.waitKey(0)