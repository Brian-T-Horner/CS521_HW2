"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem 2_1_2
This program takes a user input and tries to print it as a string,
integer and a floating-point value
"""
user_input_string = input("Please input something to be printed as a string,\
 integer and a floating-point value:")
user_input_int = int(user_input_string)
user_input_float = float(user_input_string)

print("Here is your input printed as a string: {}, as an integer: {},\
 as a float: {} ").format(user_input_string, user_input_int, user_input_float)

"""
Numeric real numbers can be used in the program without any errors,
fractions less than 1 are the exception. Ex. 4, 4.0 etc.
A number written out tho will cause an error to occur as well as
strings, non-numeric symbols etc. You could fix this with an if elif
and else loop to check the type of the input and see if it can be
converted to an int or a float. If not you could prompt an error message
to the user and continue past the loop with a new input statement after.

"""




