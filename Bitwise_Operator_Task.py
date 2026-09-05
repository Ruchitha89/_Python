"""Bitwise Operator Task : Given two integers, write a Python program that :
    - prints the result of a&b , a|b , and a^b
    - shifts the bits of a two positions to the left(a<<2)
    - shifts the bits of b one position to the right(b>>1)"""

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print("a&b:", a & b)
print("a|b:", a | b)
print("a^b:", a ^ b)
print("a<<2:", a << 2) # left shift 2 positions
print("b>>1:", b >> 1) # right shift 1 position