#-------------------------------------------------------------------------
# Name:       Guessing Game
# Purpose:    Get the user to guess a random number between 1-100 in 5 tries
# Author:     Natividad. C
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

# Define variables
tries = 4
num = random.randrange(1, 101)

# Title
print("*** Guess the Number ***")
print("Welcome to the guess the number game.")
print("You have 5 chances to guess the number between 1 and 100.\n")


while True:
    user_num = int(input("Enter a number between 1 and 100: "))
    # Check is the number is too high, low, or right
    if user_num == num and tries > 0:
        print("Congrats, you guessed it!")
        break
    elif user_num < num and tries > 0:
        print("Too low, guess again")
        tries -= 1
    elif user_num > num and tries > 0:
        print("Too high, guess again")
    else:
        break


if user_num == num and tries <= 0:        
    print(f"Sorry, you've guessed incorrectly, the number is {num}.")