#-------------------------------------------------------------------------
# Name:       Copycat
# Purpose:    Program will copy whatever the user inputs and will stop when user inputs "stop"
# Author:     Natividad. C
# Created:    08/05/2024
#-------------------------------------------------------------------------

while True:
    word = input("Enter a word: ")
    print("Your word:", word)
    if word == "stop":
        print("Goodbye!")
        break