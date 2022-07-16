from importlib.resources import Resource
import cv2
import time
import numpy as np
from tkinter import Frame
import mask
import out
from pkg_resources import resource_exists
#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)
image = cv2.imread('kim.jpg')

#Reading the captured Frame until the camera is open
while True:
    ret, img = cap.read()
    print(img)
    img = cv2.resize(img,(640,480))
    image = cv2.resize(image,(640,480))
    
    #These values can also be changed as per the color
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask_1 = cv2.inRange(Frame, u_black, l_black)

    #Keeping only the part of the images without the red color 
    #(or any other color you may choose)
    res = cv2.bitwise_and(Frame, Frame, mask=mask)

    f = Frame - Resource
    f = np.where(f == 0,image,f)
    #Displaying the output to the user
    cv2.imshow("cap", img)
    cv2.imshow('mask1',f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()