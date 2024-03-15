import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = int(input("guess a number from 1 to 10: "))
     
    if guess == num:
        print("congratulations, you guessed the number right")
        break
    elif guess > num:
        print("guess a number thats lower this time")
        
    elif guess < num:
        print("guess a number that is a little higher")