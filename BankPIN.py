#-------------------------------------------------------------------------
# Name:       Bank PIN  
# Purpose:    Gets the user to input their PIN before 
# Author:     Natividad. C
# Created:    06/05/2024
#-------------------------------------------------------------------------

# Define variables
pin = 1938

# Title
print("WELLCOME TO STA BANK!")
print(" ")

while True:
# Ask user to input their PIN
    user_pin = int(input("Enter your PIN: "))

# Check is the PIN is incorrect, if so ask to reinput
    if user_pin == pin:
        break
    else:
        print("Incorrect PIN. Try again.")

print("PIN accepted. You may now access your account.")