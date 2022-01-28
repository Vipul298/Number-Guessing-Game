import random
from wsgiref.util import guess_scheme
print("Number Gussing Game")
number = random.randint(1,9)
chances = 0
print("Guess Number (Between 1 and 9): ")

while chances < 5:

    guess = int(input("Enter Your Guess:-"))

    if (guess == number):
        print("Congratulation You Won !!!")
        break

    elif(guess < number):
        print("Your Guess Was To Low : Guess a number higher than", guess)

    else:
        print("Your Guess Was To High : Guess a number lower than", guess)

    chances += 1

    if not chances < 5:
        print("You Lose !!! The Number 1s" , number)

