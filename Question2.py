#-------------------------------------------------------------------------
# Name:       Sum of 5-20 except for multiples of 3
# Purpose:    Add numbers 5-20 without multiples of 3
# Author:     Natividad. C
# Created:    08/05/2024
#-------------------------------------------------------------------------

num = 5
sum = 0

while True:
    if num % 3 != 0:
        sum += num
    num += 1
    if num > 20:
        break

print(sum)