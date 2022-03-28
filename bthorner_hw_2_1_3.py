"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem: 2_1_3
This program take an integer from the user and preforms a calculation
with the given formula. It will then print the output using the .format
method to add commas and make the print statement have more readability.
"""
# Getting the user input and converting to an integer
n = int(input("Enter an integer:"))
# Doing calculations based on formula provided
final_number = n + n * n + n * n * n + n * n * n * n
# Printing the formula and the resulting final number
print("{0} + {0} * {0} + {0} * {0} * {0} + {0} * {0} * {0} * {0} = {1: ,}".format(n, final_number))
