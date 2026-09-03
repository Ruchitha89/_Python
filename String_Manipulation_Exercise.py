"""String Manipulation Exercise : Write a Python program that :
    - Takes a sentence as input from the user.
    - Prints the sentence in all uppercase and lowercase
    - Replaces all spaces with underscores.
    - Removes leading and trailing whitespace.
    
    Example :
    Input : "Python is awesome! "
    Output :
    Uppercase: "PYTHON IS AWESOME! "
    Lowercase: "python is awesome! "
    With underscores: "__Python_is_awesome!"
    Without whitespace: "Python is awesome!"
    Stripped :"Python is awesome!" """

# Take a sentence as input from the user

sentence = input("Enter a sentence: ")

# Print the sentence in all uppercase
print("Uppercase:", sentence.upper())

# Print the sentence in all lowercase
print("Lowercase:", sentence.lower())

# Replace all spaces with underscores
print("With underscores:", sentence.replace(" ", "_"))

# Remove leading and trailing whitespace
print("Without whitespace:", sentence.strip())