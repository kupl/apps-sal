from math import factorial
def increasing_numbers(digits):
    return factorial(9 + digits) // (factorial(digits) * factorial(9))
