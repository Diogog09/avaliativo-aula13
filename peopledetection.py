import cv2 as cv
import numpy as np
from imutils.object_detection import non_max_suppression
import imutils

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
camera = cv.VideoCapture(1)
while True:
    retval, imagem = camera.read()
    imagem = imutils.resize(imagem, width=min(600, imagem.shape[1]))
    orig = imagem.copy()
    (rects, weights) = hog.detectMultiScale(
        imagem, winStride=(4, 4), padding=(8, 8), scale=1.05)
    for (x, y, w, h) in rects:
        cv.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    for (xA, yA, xB, yB) in pick:
        cv.rectangle(imagem, (xA, yA), (xB, yB), (0, 255, 0), 2)
    print("[INFO]: {} original boxes, {} after suppression".format(
        len(rects), len(pick)))
    cv.imshow("people detector", imagem)
    k = cv.waitKey(60)  
    if k == 27: 
        break
cv.destroyAllWindows()
