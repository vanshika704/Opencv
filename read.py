import cv2 as cv 
capture = cv.VideoCapture(0)
# img = cv.imread("Images/pexels-tdcat-70912.jpg")
# cv.imshow('pexels-tdcat-70912.jpg', img)
while True:
    isTrue, frame = capture.read()
    cv.imshow ('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    capture.release()
    cv.destroyAllWindows()

cv.waitKey(0)