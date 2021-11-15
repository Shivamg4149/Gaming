def Run():
    import cv2
    import os
    import time
    import pygame
    import Hand_Detector
    import RPSGame
    pygame.init()
    pygame.mixer.music.load('music/foo.wav')
    pygame.mixer.music.play(-1)
    pTime = 0
    detector = Hand_Detector.handDetector(detectionCon=0.75)
    wCam, hCam = 640,480
    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)
    count = 0
    rock = cv2.imread("images/Rock.jpeg")
    paper = cv2.imread("images/Paper.jpeg")
    scissor = cv2.imread("images/Scissor.jpeg")
    overlaylist=[scissor,paper,rock]
    i=0
    computer_score=0
    player_score=0

    while True:
        success,img = cap.read()
        img = detector.findHands(img)
        myList = detector.findPosition(img,draw=False)
        h,w,c=overlaylist[i].shape
        img[0:h,0:w]=overlaylist[i]
        status = ""
        count+=1
        if(count<=20):
            cv2.putText(img,"1",(250,250),cv2.FONT_HERSHEY_COMPLEX,2.5,(36,255,12),6)
        elif(count<=40):
            cv2.putText(img,"2",(250,250),cv2.FONT_HERSHEY_COMPLEX,2.5,(36,255,12),6)
        elif(count<60):
            cv2.putText(img,"3",(250,250),cv2.FONT_HERSHEY_COMPLEX,2.5,(36,255,12),6)
        elif(count==60):
            if len(myList) !=0 :
                if  (myList[8][2] < myList[6][2]) and (myList[12][2] < myList[10][2]) and (myList[16][2] < myList[14][2]) and (myList[20][2] < myList[18][2]):
                    cv2.putText(img,"Paper",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(36,255,12),4)
                    status,player_score,computer_score,computer=RPSGame.Game(2,player_score,computer_score)
                elif (myList[8][2] < myList[6][2]) and (myList[12][2] < myList[10][2]):
                    cv2.putText(img,"Scissor",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(36,255,12),4)
                    status,player_score,computer_score,computer=RPSGame.Game(3,player_score,computer_score)
                else:
                    cv2.putText(img,"Rock",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(36,255,12),4)
                    status,player_score,computer_score,computer=RPSGame.Game(1,player_score,computer_score)                
                if computer==1:
                    i=2   
                elif computer==2:
                    i=1
                else:
                    i=0             
        elif(count<70):
            cv2.putText(img,status,(250,250),cv2.FONT_HERSHEY_COMPLEX,2.5,(36,255,12),6)                  
        elif(count==70):
            count=0           
        z=str(computer_score)
        st="Computer Score : "+z
        cv2.putText(img,st,(30,440),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,0),2)
        z=str(player_score)
        st="Player Score"+z
        cv2.putText(img,st,(430,440),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,0),2)
        cTime = time.time() 
        fps = 1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f'fps : {int(fps)}',(300,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()