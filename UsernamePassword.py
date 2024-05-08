#-------------------------------------------------------------------------
# Name:       Username Password
# Purpose:    
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# Define the correct username and password
correct_username = "username"
correct_password = "password"

while True:
    # Ask the user to enter username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check if both username and password are correct
    if username == correct_username and password == correct_password:
        break     
    # Check if username is incorrect
    elif username != correct_username and password == correct_password:
        print("Username incorrect")
    # Check if password is incorrect
    elif username == correct_username and password != correct_password:
        print("Password incorrect")
    # If both username and password are incorrect
    else:
        print("Username and password incorrect")

print("Welcome!")