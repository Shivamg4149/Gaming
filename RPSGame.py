import random
def Game(player,player_score,computer_score):
    rock =1
    paper =2
    scissor=3
    mylist=[]
    rule = {rock:scissor,paper:rock,scissor:paper}
    computer = random.randint(1,4)
    if player==computer:
        status = "Tied"
        mylist.append("Tied")
    else:
        if rule[player]==computer:
            mylist.append("Win")
            status="Win"
            player_score+=1
        else:
            status="Lose"
            computer_score+=1
    return status,player_score,computer_score,computer