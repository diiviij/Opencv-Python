import cv2
import numpy as np

cap = cv2.VideoCapture('Q5.mp4')
while True:
    ret, frame = cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    images = np.zeros(frame.shape , np.uint8)    
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue= np.array([30,50,30])
    upper_blue= np.array([200,255,200])
    mask = cv2.inRange(hsv, lower_blue,upper_blue)
    
    images2 = cv2.bitwise_and(frame,frame,mask = mask)


    cv2.imshow('frame',frame)
    cv2.imshow('frames',images2)
    if cv2.waitKey(1)==ord('q'):
        break


        
cap.release()
cv2.destroyAllWindows()

