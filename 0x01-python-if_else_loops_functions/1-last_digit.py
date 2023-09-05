#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = abs(number) % 10
if last_digit_str > 5:
print(f'Last digit of {number} is {last_digit_str} and is greater than 5')

elif 0 != last_digit_str < 6:
    print(f'Last digit of {number} is {last_digit_str} and is less than 6 and not 0')

else:
    print(f'Last digit of {last_digit_str} and is 0')
