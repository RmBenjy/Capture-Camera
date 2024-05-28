import cv2 as cv

# Open a connection to the camera (camera index 0 refers to the default camera)
camera = cv.VideoCapture(0)

# Start an infinite loop to continuously capture and display frames
while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Convert the image to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    

    # Apply Gaussian blur to the image
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Canny Edge Detection
    edges = cv.Canny(blur, 10, 70)
    
    # Invert the image
    inverted = cv.bitwise_not(edges)
    
    

    # Display the processed grayscale image in a window named "Us"
    cv.imshow("Sketched", inverted)

    # Check for the 'Esc' key (ASCII value 27) to break out of the loop
    if cv.waitKey(1) == 27:
        break

# Release the camera and close the window when the loop is terminated
camera.release()
cv.destroyAllWindows()
