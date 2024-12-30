# Yellow Ball Detection

## Overview
This python script processes an image to identify and highlight yellow balls. 

It applies color-based filtering in the HSV color space, detects contours, and visualizes the largest detected ball with a bounding rectangle.

## Features
- Converts the image to HSV color space for better color filtering.
- Applies a yellow color mask using specified HSV thresholds.
- Detects contours from the filtered image.
- Identifies the largest yellow ball based on contour area.
- Draws a bounding rectangle around the detected ball.
- Displays the processed image and intermediate results.

## Example Output
- Coordinates of the detected yellow ball:
  ```
  Coordinates of the yellow ball:
  (x, y), (x+w, y)
  (x, y-h), (x+w, y-h)
  Area of rectangle: w*h
  ```
  
- Displayed windows:
  - Original image with bounding rectangle.
  - Yellow mask.
  - Refined mask.
  - Masked result.
