#computer vs you game
#snake, water and gun game
import random
    
    def gameWin(comp,you):
        if comp==you:
            return None
        elif comp=='s':
            if you=='w':
                return False
            elif you=='g':
                return True
        elif comp=='w':
            if you=='s':
                return False
            elif you=='g':
                return True           
        elif comp=='g':
            if you=='w':
                return False
            elif you=='s':
                return True       
############################################
print("computer turn: enter 'w' for Water, 's' for Snake and 'g' for Gun\n")
print("computer has selected from the following w,s,g now it your turn")
randno=random.randint(1,3)
if(randno==1):
    comp="w"
elif (randno==2):
    comp="g"
elif (randno==3):
    comp="s"
#############################################
while x==1:
    you=input("your's turn select 'w' for Water, 's' for Snake and 'g' for Gun\n")
    print(f"computer choose {comp}\n")
    print(f"you choose {you}\n")
    a= gameWin(comp,you)
    if a==None:
        print("the game is a tie\n")
        x=int(input("if you want to continue the game press 1: or press 0 to exit the game")
    elif a:
        print("you won the game\n")
        x=int(input("if you want to continue the game press 1: or press 0 to exit the game")
    else:
        print("you lose!!\n")
        x=int(input("if you want to continue the game press 1: or press 0 to exit the game")
              

