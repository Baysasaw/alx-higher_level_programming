#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number)
last_digit = None
competition = None
if number < 0:
    last_digit = -int(str(number)[-1])
else:
    last_digit = int(str(number)[-1])

if last_digit > 5:
    competition = "and is greater than 5"
elif last_digit == 0:
    competition = "and is 0"
elif last_digit < 6 and not 0:
    competition = "and is less than 6 and not 0"


print(f"Last digit of {str(number)} is {str(last_digit)} {competition}")
