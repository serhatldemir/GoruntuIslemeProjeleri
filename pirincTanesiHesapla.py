import cv2



cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)


    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)


    rice_count = len(contours)
    cv2.putText(frame, f'Rice Count: {rice_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow('Rice Counting', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()