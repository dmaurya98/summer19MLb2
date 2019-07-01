import cv2
import numpy as np

# starting camera
camera = cv2.VideoCapture(0)

# checking camera is open or not
if camera.isOpened():
    print('Camera opened.')
else:
    print('Camera not opened.')

# taking input from camera
status, frame1 = camera.read()
status, frame2 = camera.read()

# displaying
cv2.imshow('Frame1', frame1)
cv2.imshow('Frame2', frame2)
cv2.waitKey(0)

# to close camera
camera.release()
