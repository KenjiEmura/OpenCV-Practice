import cv2

print("Package imported")

# img = cv2.imread("Resources/picture.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# ------------------------------------------------

# Saved video file:
# video = cv2.VideoCapture("Resources/video.mp4")

# while True: 
#   success, img = webcam.read()
#   cv2.imshow("Video", img)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

# ------------------------------------------------

# Webcam stream (apparently not working with Python 3.9)
webcam = cv2.VideoCapture(0)
# The number 3 corresponds to the width and 4 to the heigth
# webcam.set(3, 640)
# webcam.set(4, 480)

print("We got here...")
print(webcam)

while True: 
  success, img = webcam.read()
  cv2.imshow("Video", img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  