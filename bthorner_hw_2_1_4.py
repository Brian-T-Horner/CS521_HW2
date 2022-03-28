"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem: 2_1_4
This program takes an inputed integer and tells if it is even or odd
based on a boolean comparison it then prints 1 or 0 for True or False
respectively.
"""


user_input_string = input("Please enter an integer:")
user_input_int = user_input_string
print(int(bool(user_input_int % 2 == 0)))

"""
We take the input as a string and then convert it to an integer. We then evaluate user inputed integer to see if it is even.If this is true the
bool of True or False is returned.
"""

"""
Here I made the program functionable in 2 lines to show how you can
refactor it down even further. While the readability is lower I think
the trade off here is worth it. Unlike the one below.
"""

user_input_int_2 = int(input("Please enter an integer again:"))
print(int(bool(user_input_int_2 % 2 == 0)))


"""
Here is the same problem solved using one line of code. I don't think it
is very readable but it solves the problem and has the functionality.
"""
print(int(bool((int(input("Please enter an integer another time:"))) % 2 == 0)))
