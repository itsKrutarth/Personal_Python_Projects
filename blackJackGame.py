import random
from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
compDraws = []
userDraws = []

def checkForCompCards(comp):
    while (comp <= 16):
        compDraw = cards[random.randint(0, len(cards)-1)]
        if (compDraw == 11):
            if (comp + compDraw > 21):
                compDraw = 1
            compDraws.append(compDraw)
            comp += compDraw
    return comp


def checkForWinUser(user, comp):
    if(user<21):
        checkForCompCards(comp)
    return user, comp

print("lets start BlackJack game!")

step = ""
user = []
comp = []
print("First Draw!")
userSum = 0
compSum = 0
count =1
while (step !="no"):
    userDraw = cards[random.randint(0, len(cards)-1)]
    compDraw = cards[random.randint(0, len(cards)-1)]
    if(userDraw == 11 or compDraw ==11):
        if (userSum+userDraw > 21):
            userDraw=1
        if (compSum + compDraw > 21):
            compDraw = 1
    userSum+=userDraw
    compSum +=compDraw
    userDraws.append(userDraw)
    compDraws.append(compDraw)
    print(f"Your draws so far: {userDraws}, and total is: {userSum}")
    if(userSum>21):
        print("You loose!")
        print(f"Computer's draws: {compDraws}")
        break
    if(count==1):
        print(f"Computer's draw: {compDraw}, and total is: {compSum}")
    if count>1:
        step=input("Would you like to Hit another draw? yes or no?:")
    if(step=="no"):
        userCheck, compCheck = checkForWinUser(userSum, compSum)
        print(f"Computer's draws: {compDraws}")
        if(userCheck==compCheck):
            print("DRAW!")
        elif(userCheck<compCheck):
            print("YAYYY YOU WON!!")
        else:
            print("You loose!")
    count+=1
