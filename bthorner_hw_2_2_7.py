"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem: 2_2_7
I rewrote the commented out 'for loop' as a 'while loop'.
the while loop starts with a default value that is incremented after
the loop is finished until it reaches a value of 11 which stops the loop
The functionality of the 'while loop' is the same as the 'for loop'.
"""

# X = 10
# for i in range(1, X + 1):
#     if X % i == 0:
#         print(i)

X = 10
current_value = 1

while current_value <= X:
    if X % current_value == 0:
        print(current_value)
    current_value += 1
