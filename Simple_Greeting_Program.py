"""Simple Greeting Program : Write a python program that asks  the user for their name and age,then prints a personalized greeting 
message.Use both the + operator and f-strings for output.

Example : 
    Enter your name: Alice
    Enter your age: 25
    output: Hello, Alice! You are 25 years old.
"""

# Ask user for their name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# using + operator for output
print("Hello, " + name + "! You are " + age + " years old.")

# using f-strings for output
print(f"Hello, {name}! You are {age} years old.")