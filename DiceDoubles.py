#-------------------------------------------------------------------------
# Name:       Dice Doubles
# Purpose:    Rolls dice until both dice are the same number
# Author:     Natividad. C
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

# Define variable
roll_1 = random.randrange(1, 7)
roll_2 = random.randrange(1, 7)

# Title
print("HERE COMES THE DICE!")
print(" ")

# Loop until both variables are equal
while True:
    roll_1 = random.randrange(1, 7)
    roll_2 = random.randrange(1, 7)
    print(f"Roll #1: {roll_1}")
    print(f"Roll #2: {roll_2}")
    print(f"The total is {roll_1 + roll_2}!")
    print(" ")
    if roll_1 == roll_2:
        break