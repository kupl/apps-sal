import math


def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    if n > 0:
        return math.factorial(n)
