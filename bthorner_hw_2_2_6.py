"""
Brian Horner
CS 521 - Summer 1
Date: 5/25/2021
Homework Problem: 2_2_6
This program calculates and prints all the leap years from 1899 to 2021 using 'for loop' and a 'while loop'.
I used empty lists to contain the years from the list in order to make the data more readable
I believe the output follows the guide of all year resuts on one comma seperated outputs
"""


# creating the empty lists and the current_year variable
current_year = 1899
leap_year = []
not_leap_year = []

# Starting the 'for loop'.
# If the year passes the leap year conditions,
# it is added to the leap_year list
# If the year does not pass the leap year conditions it is added to the not_leap_year list
for current_year in range(current_year, 2021 + 1):
    if current_year % 4 == 0:
        if current_year % 100 == 0:
            if current_year % 400 == 0:
                leap_year.append(current_year)
            else:
                not_leap_year.append(current_year)
        else:
            leap_year.append(current_year)
    else:
        not_leap_year.append(current_year)

# Printing the lists without the brackets
print("'for loop' Leap Years:", str(leap_year)[1:-1])
print("\n 'for loop' Not Leap Years:", str(not_leap_year)[1:-1])


# Establishing the current_year_2 variable and the empty lists
current_year_2 = 1899
leap_year_2 = []
not_leap_year_2 = []

"""
This code below is using a while loop to determine leap years from 1899
to 2021
"""

# This loop appends the apporpriate lists for the years as well
while current_year_2 <= 2021:
    if current_year_2 % 4 == 0:
        if current_year_2 % 100 == 0:
            if current_year_2 % 400 == 0:
                leap_year_2.append(current_year_2)
            else:
                not_leap_year_2.append(current_year_2)
        else:
            leap_year_2.append(current_year_2)
    else:
        not_leap_year_2.append(current_year_2)
    current_year_2 += 1

# Printing the lists with some formating
print("\n 'while loop' Leap Years:", str(leap_year_2)[1:-1])
print("\n 'while loop' Not Leap Years:", str(not_leap_year_2)[1:-1])
