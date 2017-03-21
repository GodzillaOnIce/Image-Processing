'''
Created on Mar 1, 2017

Look at this tutorial: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_trackbar/py_trackbar.html

@author: JC
'''

# Import libraries
import cv2 as cv

# Create a nothing function to make arguement 5 on createTrackbar happy
def nothing(x):
    pass

# Load image to memory 
image = cv.imread("angry.jpg")
image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# Create a named Window
nm = cv.namedWindow("MyWindow")

# Create our trackbar on our Window
cv.createTrackbar("Threshold","MyWindow",0,255,nothing)

# Create a while loop to continuously show the result of our image
while True:
    # Fetch the current value of our trackbar
    t_val = cv.getTrackbarPos("Threshold","MyWindow")

    # Threshold our image using the value from the trackbar
    ret, thresholdedImg = cv.threshold(image.copy(),t_val,255,cv.THRESH_BINARY)
    
    # Write some text on the image
    cv.putText(thresholdedImg,"PRESS Q TO EXIT",(5,20),cv.FONT_HERSHEY_PLAIN,1.0,(0,0,0))
    
    # Show the image
    cv.imshow("MyWindow",thresholdedImg)
    
    # Listen for the q button being pressed
    if cv.waitKey(1) == ord('q'):
        #Break out of the main loop
        break

# Clean Up
cv.destroyAllWindows()

