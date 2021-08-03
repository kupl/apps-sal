import math


def am_i_wilson(n):
    if n < 2 or n > 563:
        return False
    return (math.factorial(n - 1) + 1) % (n**2) == 0
