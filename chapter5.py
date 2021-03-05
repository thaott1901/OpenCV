import cv2
import numpy as np

img = cv2.imread("rsc/paper.jpg")

width,height = 500, 700
pts1 = np.float32([[342, 331], [36, 713], [701, 410], [490, 948]])
pts2 = np.float32([[0, 0], [0, height], [width, 0], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Img", img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
