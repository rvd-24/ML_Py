import cv2
import time
import os
import HandTrackingModule as htm
wCam,hCam=640,480;
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

pTime=0

detector=htm.handDetector()
tipIds=[4,8,12,16,20]
while True:
    success,img=cap.read()
    img=detector.findHands(img);
    lmlist=detector.findPosition(img,draw=False)
    # print(lmlist)

    if len(lmlist)!=0:
        fingers=[]
        #Thumb
        if lmlist[tipIds[0]][2]<lmlist[tipIds[0]-1][2]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2]<lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,f'FPS:{int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow("Img",img)
    cv2.waitKey(1);