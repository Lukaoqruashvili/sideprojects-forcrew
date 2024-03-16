import random

computerchoices = ['rock', 'paper', 'scissors']

userchoice = input("choose rock, paper or scissors: ")

randomchoice = random.choice(computerchoices)

print('the computer chose:' + randomchoice)
print('you chose:' + userchoice)

if userchoice == randomchoice:
    print("tie")

elif userchoice == "rock" and randomchoice == "scissors":
    print("you win")

elif userchoice == "scissors" and randomchoice == "paper":
    print("you win")

elif userchoice == "paper" and randomchoice == "rock":
    print("you win")

else:
    print("the computer wins")
    