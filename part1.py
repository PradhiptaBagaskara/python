import numpy as np
import cv2

cap = cv2.VideoCapture('sur.m4v') #Open video file or use 0 for webcam

while(cap.isOpened()):
    ret, frame = cap.read() #read a frame
    # show frame
    cv2.imshow('Frame',frame)

    #Abort and exit with 'Q' or ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #release video file
cv2.destroyAllWindows() #close all openCV windows

