import cv2 as cv  # importing cv2 as cv

# img = cv.imread("Images/pexels-tdcat-70912.jpg")
# cv.imshow('pexels-tdcat-70912.jpg', img)
capture = cv.VideoCapture(0)  # creating a capture object and opening webcam

while True:  # continuously capturing video frames
    isTrue, frame = capture.read()  # reading the video frame by frame

    if not isTrue:
        break  # if frame is not captured properly, exit the loop

    cv.imshow('Video', frame)  # displaying the video frame

    if cv.waitKey(20) & 0xFF == ord('d'):  # if 'd' key is pressed, break the loop
        break

capture.release()  # releasing the capture object
cv.destroyAllWindows()  # closing all OpenCV windows
