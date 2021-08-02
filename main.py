import cv2
#imported openCV
import numpy as np
#imported numpy
from pyzbar.pyzbar import decode
#imported pyzbar

print("[INFO] starting the cam....")
#displaying the camera funtion
cap = cv2.VideoCapture(0)
#opening cam
cap.set(3,640)
#height of cam window
cap.set(4,360)
#width of cam window
print("[INFO] Scaning code....")
with open('ABC.txt') as f:
    myDataList = f.read().splitlines()
#reading the text file which contains authorized and unauthorized codes
while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            print('Authorized')
            myColor = (0,255,0)
#printing authorized code
        else:
            print('Un-Authorized')
            myColor = (0, 0, 255)
#printing unauthorized code
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_ITALIC,
                    0.9,myColor,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
