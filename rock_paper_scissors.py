#rock paper scissors game using rondom function.

#rock with scissors is win for rock.
#rock with paper is win for paper.
#rock with rock is draw.

#paper with scissors is win for scissors.
#paper with paper is draw.
#paper with rock is win fo paper.


#scissors with rock is win for rock.
#scissors with paper is win for scissors.
#scissors with scissors is draw.

import random

#global declaration
ywins = 0
cwins = 0
i = 0
print("You have 5 chances to play")
# functions for printing
def you_won():
    print("you won ")
    global ywins
    ywins = ywins + 1

def c_won():
    print("computer won")
    global cwins
    cwins = cwins + 1

def you_l():
    print("\nYOU LOST THE GAME")

def c_l():
    print("\nYOU WON THE GAME")

#logic
while(i<=5):
    you = input("\nEnter 1 = rock, 2 = paper or 3 = scissors:")
    if you == "1":
         print("you chose rock")
    if you == "2":
        print("you chose paper")
    if you == "3":
        print("you chose scissors")
    options = ["rock","paper","scissors"]
    computer = random.choice(options)
    print("computer chose",computer)
    if computer == "rock" and you == "1" or computer == "paper" and you == "2" or computer == "scissors" and you == "3":
        print("Draw")
    elif computer == "rock" and you == "2":
        you_won()
    elif computer == "rock" and you == "3":
        c_won()
    elif computer == "paper" and you == "1":
        c_won()
    elif computer == "paper" and you == "3":
        you_won()
    elif computer == "scissors" and you == "1":
        you_won()
    elif computer == "scissors" and you == "2":
        c_won()
    else:
        print("invalid option")
        exit()
    i = i + 1

#results
print("\ncomputer won",cwins,"times")
print("you won",ywins,"times")

#declaration
if cwins > ywins:
    you_l()
elif ywins > cwins:
    c_l()

