import cv2

img = cv2.imread("Resources/picture.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# (7,7) is the kernel size, the 0 is the sigma (no idea what that means)
imgBlur = cv2.GaussianBlur(imgGray, (99, 99), 0)

# Edge detection:
imgCanny = cv2.Canny(img, 250, 200)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)