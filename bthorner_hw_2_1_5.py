"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem: 2_1_5
This program calculates a users Body Mass Index(BMI) from the user
inputed weight and height
(In weight is in kilograms and height is in meters)
"""

# Grabbed the two inputs
# Weirdly enough when trying to run using sudo python in terminal an EOF
# error occurs. Not sure why. Running with just python works

user_input_weight_str, user_input_height_str = input(
    "Please enter your weight in kilograms and height in meters (seperated by a space): ").split()

# Converted the strings into floats
user_weight_float = float(user_input_weight_str)
user_height_float = float(user_input_height_str)

# Calculating BMI
user_bmi_float = user_weight_float / (user_height_float**2)

# Printing user inputs and BMI with two decimal places for each
print("Body Mass Index (BMI) for Weight {0:.2f} and Height {1:.2f} is {2:.2f}".format(
    user_weight_float, user_height_float, user_bmi_float))
