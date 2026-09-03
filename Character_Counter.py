"""Character Counter : Write a Python program that :
    - Asks the user for a string
    - Prints how many characters are in the string, excluding spaces.
    Example :
    Input : "Hello World"
    Output : "Number of characters (excluding spaces): 10"
"""

# Ask the user for a string
text = input("Enter a string: ")

# Remove spaces 
no_spaces = text.replace(" ", "")

# Count characters
count = len(no_spaces)

# Print the result
print(f"Number of characters (excluding spaces): ",count)