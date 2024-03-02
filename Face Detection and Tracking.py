# Importing OpenCV package 

import cv2 

# Loading the required haar-cascade xml classifier file
alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0) #Obtain feed from camera


while True:
    _,img = cam.read() #Read from the Camera
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Converting image to grayscale 
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),5) # print(contours)
    cv2.imshow("FaceDetection",img)  #Iterating through rectangles of detected faces 
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
