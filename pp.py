import cv2
import numpy as np

cap = cv2.VideoCapture('Q8.mp4')
while True:
    ret, frame = cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    image= np.zeros(frame.shape , np.uint8)    
    smaller_frame =cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    image[:height//2, :width//2]=smaller_frame    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue= np.array([30,50,30])
    upper_blue= np.array([200,255,200])
    mask = cv2.inRange(hsv, lower_blue,upper_blue)
    image = cv2.bitwise_and(frame,frame,mask = mask)
    
    image[:height//2, width//2:]=smaller_frame
  

    cv2.imshow('frames',image)
    if cv2.waitKey(1)==ord('q'):
        break


        
cap.release()
cv2.destroyAllWindows()

