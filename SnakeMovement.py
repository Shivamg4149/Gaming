def SnakeMovement(x1,x2,y1,y2,flag,snake_block):
    '''if(flag==0):
        px = myList[9][1]
        py = myList[9][2]
        flag=1'''
    px=x1
    py=y1
    cx = x2
    cy = y2
    dx = cx-px
    dy = cy-py
    px = cx
    py = cy
        #print(dx,dy)
    if(dx>20):
        #print("Move Left")
        x1_change = -snake_block
        y1_change = 0
        #cv2.putText(img,"Left",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),3)
        return px,py,x1_change,y1_change,"Left"
    elif(dx<(-20)):
        #print("Move Right")
        x1_change = snake_block
        y1_change = 0
        #cv2.putText(img,"Right",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),3)
        return px,py,x1_change,y1_change,"Right"
    elif(dy>20):
        #print("Move Down")
        y1_change = snake_block
        x1_change = 0
        #cv2.putText(img,"Down",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),3)
        return px,py,x1_change,y1_change,"Down"
    elif(dy<(-20)):
        #print("Move Up")
        y1_change = -snake_block
        x1_change = 0
        #cv2.putText(img,"Up",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(255,255,255),3)
        return px,py,x1_change,y1_change,"Up"
    return px,py,""