import cv2 as cv # iimport cv2 as cv

# img = cv.imread('Images/pexels-tdcat-70912.jpg') #image ko read kro
# cv.imshow('Cat', img )

def rescaleFrame(frame ,  scale=0.75):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)
    dimensions = (width,height)
    return cv.resize(frame ,  dimensions , interpolation = cv.INTER_AREA)


capture = cv.VideoCapture('videos/4811927-hd_1920_1080_30fps.mp4')
while True:
    isTrue , frame = capture.read()
    resized_frame = rescaleFrame(frame)
    cv.imshow ('Video', frame)
    cv.imshow('video_resized', resized_frame)
    if cv.waitKey(20) & 0xFF==ord('d'): # specifications hai samajh  meko aai nahi
        break # break condition lgdi

capture.release()
cv.destroyAllWindows()


