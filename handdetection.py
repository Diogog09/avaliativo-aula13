import cv2 as cv

camera = cv.VideoCapture(1)

cascade = cv.CascadeClassifier("palm_v4.xml")
cascade2 = cv.CascadeClassifier("closed_frontal_palm.xml")

while True:
    _,image = camera.read()
    image = cv.flip(image,1)
    blur = cv.GaussianBlur(image,(7,7),0)
    gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)

    detect = cascade.detectMultiScale(gray,1.2,5)
    detect2 = cascade2.detectMultiScale(gray,1.2,5)

    for (x,y,w,h) in detect:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    for (x,y,w,h) in detect2:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)


    cv.imshow("Palm Hand", image)

    k= cv.waitKey(60)
    if k == 27:
        break

cv.destroyAllWindows()
camera.release()