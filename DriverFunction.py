def Game():
    import cv2
    import time
    import os
    import cv2
    import mediapipe as mp
    import time
    import RockPaperScissor
    import Snake
    import Hand_Detector

    detector = Hand_Detector.handDetector(detectionCon=0.75)
    wCam, hCam = 640,480
    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)

    list_of_game=["Rock Paper Scissor","Snake","Flappy Bird","Car Race","Game 5"]

    number=len(list_of_game)
    print(number)

    flag=0

    highlight=0
    print(list_of_game[highlight])

    x=100
    y=100
    j=0

    quit=False

    while True:#success:
        success,img = cap.read()
        #print(img)
        count=0
        img = detector.findHands(img)
        myList = detector.findPosition(img,draw=False)

    #     j=0
        while count<=15:
            status,img = cap.read()
            img = detector.findHands(img)
            myList = detector.findPosition(img,draw=False)
            y1=0
            for i in list_of_game:
                if(list_of_game[highlight]==i):
                    cv2.putText(img,i,(x,y+y1),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,255,12),2)
                    y1+=40

                else:
                    cv2.putText(img,i,(x,y+y1),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,12),2)
                    y1+=40

            if(len(myList)!=0):
                if(flag==0):
                    px = myList[9][1]
                    py = myList[9][2]
                    flag=1
                cx = myList[9][1]
                cy = myList[9][2]
                dx = cx-px
                dy = cy-py
                if(dy>20):
                    j=2
                    #print("Move Down")
                elif(dy<(-20)):
                    j=1
                    #print("Move Up")
                elif(dx<(-20)):
                    j=3
                    break

                px = cx
                py = cy
            cv2.imshow("Image",img)
            count+=1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if(j==2):
            if(highlight<number-1):
                highlight+=1

        elif(j==1):
            if(highlight>0):
                highlight-=1

        count=0
        if(j==3):
            print(highlight+1)
            highlight+=1
            break

        j=0
    cap.release()   
    cv2.destroyAllWindows()
    if(highlight==1):
        RockPaperScissor.Run()
    elif(highlight==2):
        Snake.Game()
    elif(highlight==3):
        import FlappyBird
        FlappyBird.DriverGame()
    elif(highlight==4):
        import CarRace
        CarRace.gameloop()