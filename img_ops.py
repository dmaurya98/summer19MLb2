import cv2
import sys

# printing cv2 version
print("OpenCV version: " + cv2.__version__)

# taking image from argument
data = sys.argv[1]

# reading image
img = cv2.imread(data, 0)

# printing image shape
print(img.shape)

# displaying image
cv2.imshow('Image1', img)
cv2.imshow('Image2', img + 50)
cv2.imshow('Image3', img - 50)
cv2.imshow('Image4', img[200:, 300:] + 20)
cv2.imshow('Image5', img / 50)

# waiting for key press
cv2.waitKey(0)
