#-------------------------------------------------------------------------
# Name:       Skip 7
# Purpose:    Print numbers 1-10 while skipping 7
# Author:     Natividad. C
# Created:    08/05/2024
#-------------------------------------------------------------------------

num = 1

while True:
    if num != 7:
        print(num)
    num += 1
    if num > 10:
        break