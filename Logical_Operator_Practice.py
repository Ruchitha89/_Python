"""Logical Operator Practice : Write a Python program that takes two numbers as input from the user and checks if:
    - Both numbers are greater than 10(using and)
    - At least one of the numbers is less than 5(using or)
    - The first number is not greater than the second(using not)"""

# Taking two numbers as input from the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# 1) Both numbers are greater than 10 (using and)

print("Both numbers are greater than 10:", a > 10 and b > 10)

# 2) At least one of the numbers is less than 5 (using or)

print("At least one number is less than 5:", a < 5 or b < 5)

# 3) First number is not greater than the second (using not)

print("First number is not greater than the second:", not (a > b))