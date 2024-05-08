#-------------------------------------------------------------------------
# Name:       Start to End
# Purpose:    Asks the user for a starting number and an ending number, then calculates the sum of all the numbers from the start to the end, but stops if it encounters a 13 or a 31:
# Author:     Natividad
# Created:    08/05/2024
#-------------------------------------------------------------------------

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

total = 0
num = start

while num <= end:
    if num == 13 or num == 31:  # Check if the number is 13 or 31
        break
    total += num
    num += 1

print(f"The sum up to the point of encountering 13 or 31 is: {total}")