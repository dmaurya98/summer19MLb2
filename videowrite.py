import cv2
import numpy as np

# starting camera
camera = cv2.VideoCapture(0)

# adding plugging
four_cc = cv2.VideoWriter_fourcc(*'XVID')

# creating video writer
writer = cv2.VideoWriter('class.avi', four_cc, 25, (640, 480))

# checking camera is open or not
if camera.isOpened():
    print('Camera opened.')
else:
    print('Camera not opened.')

while True:
    _, frame = camera.read()

    # displaying frame
    cv2.imshow('Recorder', cv2.flip(frame, 1))

    # writing to video
    writer.write(cv2.flip(frame, 1))

    if cv2.waitKey(25) & 0xff == ord('q'):
        break

# to close camera and window
cv2.destroyAllWindows()
camera.release()
writer.release()

print('Camera closed.')
print('Video created.')
