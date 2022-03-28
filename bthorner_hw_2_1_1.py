"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem: 2_1_1
This program takes a user inputed integer and adds 2, multiplys it by 3, subtracts 6 and divides 3. After it will check if the original number is
the same as calculated number. It prints the result to the user.
"""

user_input_float = float(input("Input a number for manipulation: "))
calculated_float = ((user_input_float + 2) * 3 - 6) / 3

if calculated_float == user_input_float:
    print("The first inputed number: {0} and the first calculated value: {1} are equal in value".format(
        user_input_float, calculated_float))
else:
    print("The first inputed number: {0} and the first calculated value: {1} are not equal in value".format(
        user_input_float, calculated_float))

"""
The problem with this program structure is if you convert the user input
to a float and try the calculations it will not be equal to the original
value. I tried to avoid this by simply converting any user input to an
integer which would allow the program to work.


Further more I decided to try a different solution which uses what we
learned from reading about the decimal module. It determines the
equality through checking  if the absolute value of the difference is
within an accepted value.
I made it so that there are 20 decimal places for accurate comparison.

Please let me know if I am applying this correctly. I believe I can
refactor this down further and clean it up but I've spent to much time
messing around with this module.

"""

import decimal
from decimal import Decimal
from decimal import localcontext

with localcontext() as context:
    context.prec = 20

# context.rounding = ROUND_CEILING
    user_input_decimal = Decimal.from_float(float((
        input("Please enter a number for calculations: "))))

    number_final_decimal = Decimal((user_input_decimal + 2) * 3 - 6) / 3

    if abs(number_final_decimal - user_input_decimal) < 0.00001:
        print("The second original number: {0} and the second calculated value: {1} are equal in value.".format(
            user_input_decimal, number_final_decimal))
    else:
        print("The second original number: {0} and the second calculated value: {1} are not equal in value".format(
            user_input_decimal, number_final_decimal))
