import cv2
import numpy as np

# starting camera
camera = cv2.VideoCapture(0)

# checking camera is open or not
if camera.isOpened():
    print('Camera opened.')
else:
    print('Camera not opened.')

while True:
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)

    cv2.line(frame, (0, 0), (100, 100), (0, 255, 0), 1)
    cv2.rectangle(frame, (50, 50), (80, 80), (0, 0, 255), 1)
    cv2.circle(frame, (100, 100), 20, (255, 0, 0), 1)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'OpenCV', (10,200), font, 4, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow('BGR', frame)    
    cv2.imshow('Grey', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    if cv2.waitKey(25) & 0xff == ord('q'):
        break

# to close camera and window
cv2.destroyAllWindows()
camera.release()

print('Camera closed.')
