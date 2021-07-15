from math import floor

def isMultiple(a, b, n):
    fractional_part = floor(10 * (a/b - a//b) + 0.5)
    if fractional_part == 10:
        fractional_part //= 10 
    return fractional_part and fractional_part % n == 0
