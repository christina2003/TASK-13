## Color Detection Part
As a first step toward implementing color detection the test image is converted from RGB to HSV by the following line:

```img_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)```
### Color Ranges
The ranges in HSV of colors which are in the test image are defined in the code to be used in the rest of it.
```color_ranges = {
    "Red": ([0, 100, 100], [10, 255, 255]),
    "Green": ([36, 100, 100], [86, 255, 255]),
    "Blue": ([100, 100, 100], [140, 255, 255]),
    "Yellow": ([20, 100, 100], [30, 255, 255])
}
```
### Masks 

This part is written to iterate on the pixels of the test image and the ranges of colors, To create color mask which will help in the shape detection.


---------------------------------------------------

## Shape Detection Part  
### Noise Reduction (Blurring) 
A Gaussian blur is applied to the color mask to reduce noise. Small imperfections in the mask could lead to the detection of false contours. Blurring helps smooth out the image and minimize these small errors, improving the accuracy of shape detection

### Contour Detection
- Contours are detected using ```cv2.findContours``` . Contours are the boundaries or outlines of shapes detected in the image, which we use to analyze the geometric properties of each shape

### Polygon Approximation (Simplifying Contours)
- ```cv2.approxPolyDP``` : This function approximates the contour shape to a polygon with fewer vertices, simplifying the contour to its most basic form. 
    - epsilon represents the maximum distance between the original contour and the approximated polygon. It controls the level of detail retained from the contour
    - A smaller epsilon will make the polygon closely match the actual contour, while a larger epsilon will result in a more simplified polygon, possibly ignoring minor details
- In our case, we set epsilon to be a fraction of the contour’s arc length (perimeter) to balance accuracy and simplicity. This allows us to ignore very small deviations in the shape and focus on the overall shape structure , and the function returns a set of vertices that define the simplified shape.
 
### Draw Contours
```cv2.drawContours``` : It is used to draw the contours of each shape in the image

### Shape Detection
 we detect the shape based on the number of vertices (corners):
- 3 vertices: A triangle.
- 4 vertices: Could be either a square or rectangle.
    - The aspect ratio is used (width divided by height) to differentiate:
    - If the aspect ratio is close to 1 (between 0.95 and 1.05), the shape is a square.
    - If the aspect ratio is outside this range, the shape is a rectangle.
- More than 4 vertices: This is classified as a circle (or any round shape). If a shape has many vertices, it’s generally closer to a circle in its approximation.

### Labeling the Shape and color
The detected shapes are labeled in the image using ```cv2.putText``` function
