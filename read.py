import cv2 as cv  #import kiya cv2 ko as cv

# img = cv.imread("Images/pexels-tdcat-70912.jpg")
# cv.imshow('pexels-tdcat-70912.jpg', img)
capture = cv.VideoCapture(0) # capture naam ka variable bnaya , usme cv.Videocapture ki property lgadi or set krdiya usko 0 pe , jisme 0 web cam ka no hota h , toh is case me ye  webcam kholke dega
while True: # condition lgai while true ki or neeche  value pass krdi true 
    isTrue, frame = capture.read() # ab kuki condition true hai , toh kya kro bhyi? read kroge na video ko , toh capture varable ko read property lgadi

    cv.imshow ('Video', frame) # ab capture toh krlia , show bhi toh krna h , toh imshow krke video ko , frame ko show krdiya

    if cv.waitKey(20) & 0xFF==ord('d'): # specifications hai samajh  meko aai nahi
        break # break condition lgdi
    capture.release()
    cv.destroyAllWindows()

# cv.waitKey(0)