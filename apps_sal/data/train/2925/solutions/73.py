import math


def multiply(n):
    sum = n * 5
    digits = len(str(n))
    if n < 0:
        digits = digits - 1
    for x in range(digits - 1):
        sum = sum * 5
    return sum
