import random
secret= random.randint(1,100)
atttempts=7
print("welcome to the number guessing game")
print("guess a number from 1 to 100")
print("you have 7 attempts to guess the number")
while > 0
guess=int(input("enter your guess,"))
if guess==secret
print=("congratulations you find the number correctly")
break
elif guess< secret
print("TOO LOW")
else guess>secret
print("TOO HIGH")
attempts -=1
print("attempts left:",attempts
if attempts==0
print("game over")
print("The correct number was:",secret)
break
      
