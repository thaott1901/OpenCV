import cv2
import numpy as np
print("Package imported")

# import a picture
# img = cv2.imread("rsc/salter.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# import a video
# cap = cv2.VideoCapture("rsc/non.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # using webcam
# cap = cv2.VideoCapture(0)
# # width, id = 3
# cap.set(3, 640)
# # height, id = 4
# cap.set(4, 640)
# # brightness, id = 10
# cap.set(10, 100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# chapter 2
img = cv2.imread("rsc/salter.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
imgCanny = cv2.Canny(img, 75, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=5)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)