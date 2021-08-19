# Goal: Write a program that determines whether an integer n is divisible by integers x and y and has no remainder.
# The program should return a True or False value.
# General Strategy: Check to see if the remainder value of n / x and n / y is equivalent to zero.
# Use modulus to find the remainders.
# To return a boolean value of both remainders being zero, I can add both remainders together.
# This will work because if both are zero the sum will be zero.
# If not then the sum will be different and the boolean value returned will be false.

def is_divisible(n, x, y):
    # Return a boolean value by checking to see whether the sum of the remainders of n modulus x and n modulus y equals
    # zero.
    return 0 == (n % x) + (n % y)
