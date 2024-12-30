import cv2 as cv
import numpy as np

# Load image
img = cv.imread(r"C:\Users\ealmi\Desktop\opencv\buoy.png", cv.IMREAD_COLOR)

# Convert to HSV color space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Create yellow filter
lower_yellow = np.array([15,70,100]) 
upper_yellow = np.array([30,255,255])  

# 1- Create a mask for yellow color
kernel = np.ones((5, 5), np.uint8) 

mask = cv.inRange(hsv, lower_yellow, upper_yellow)

dilation = cv.dilate(mask, kernel, iterations = 1)
closing = cv.morphologyEx(dilation, cv.MORPH_CLOSE, kernel)

res = cv.bitwise_and(img, img, mask=closing)

# 2- Find contours from the yellow mask
#Contours can be explained simply as a curve joining all the continuous points, having same color or intensity.
contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 3- Find largest yellow ball
if contours:
    largest_contour = max(contours, key=cv.contourArea)

    # 4- Compute the bounding rectangle around the largest contour
    x, y, w, h = cv.boundingRect(largest_contour)

    # 5- Draw a green rectangle around the ball
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 6- write coordinates of the ball and the rectangle
    print(f"Coordinates of the yellow ball:\n{(x,y)}{(x+w,y)}\n{(x,y-h)}{(x+w,y-h)} ")
    print(f"Area of rectangle: {w*h}")
else:
    print("No contours found")

# Show images
cv.imshow("img", img)
cv.imshow("mask", mask)
cv.imshow("closing", closing)
cv.imshow("res", res)

# Wait for key press and close windows
cv.waitKey(0)
cv.destroyAllWindows()
