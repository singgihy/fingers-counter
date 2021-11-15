from cvzone.HandTrackingModule import HandDetector
import cv2
import serial
serialcomm = serial.Serial('/dev/ttyUSB0', 9600)
serialcomm.timeout = 1

cap = cv2.VideoCapture(0)
detector= HandDetector(detectionCon=1, maxHands=2)
while True:
    
    success, img=cap.read()

    hands, img=detector.findHands(img)

    if hands:
        hand1=hands[0]
        lmList1=hand1['lmList']
        centerPoint1 = hand1['center']
        handType1=hand1['type']
        fingers1=detector.fingersUp(hand1)
        jmlfingers1=sum(fingers1)
        e='\n'
        print(jmlfingers1)
        serialcomm.write(e.encode())
        serialcomm.write(str(jmlfingers1).encode())

        if len(hands)==2:

            hand2=hands[1]
            lmlist2=hand2['lmList']
            centerPoint2 = hand2['center']
            handType2=hand2['type']
            fingers2=detector.fingersUp(hand2)
            jmlfingers2=fingers2
            e='\n'
            print(jmlfingers2)
            serialcomm.write(e.encode())
            serialcomm.write(str(jmlfingers2).encode())

    cv2.imshow("image",img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()