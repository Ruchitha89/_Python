""" Write a Python program that swaps the values of two variables with and without using a temporary(third) variable. """

# Swapping values using a temporary(Third) variable

a = 10
b = 20
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# Swapping without using a temporary variable

a = 30
b = 40
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping without a temporary variable
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
