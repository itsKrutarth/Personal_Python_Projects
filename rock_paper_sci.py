#list practice
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
user = int(input("Enter your choice. Rock = 1, Paper = 2, and Scissors = 3. Enter number: "))
print(game[user-1])
comp = random.randint(1,3)
print (game[comp-1])
if (user==comp):
    print("Tie")
elif(user<comp and (user!=1 or comp!=3)):
    print("You loose")
elif(comp<user and (comp !=1 or user !=3)):
    print("You Won")
elif(user==1 and comp==3):
    print ("You Won!")
elif(comp ==1 or user ==3):
    print("You loose!")