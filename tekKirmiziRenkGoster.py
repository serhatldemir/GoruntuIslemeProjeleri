import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])


    red_mask = cv2.inRange(hsv, lower_red, upper_red)


    result = cv2.bitwise_and(frame, frame, mask=red_mask)


    cv2.imshow('Original', frame)
    cv2.imshow('Only Red Objects', result)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()