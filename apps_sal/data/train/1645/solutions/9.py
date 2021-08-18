import math


def is_perfect_sq(n):
    sr = math.sqrt(n)
    low_perfect = math.floor(sr)
    check = sr - low_perfect == 0
    return check


def sum_of_squares(n):
    """ 
    Based on 
    1. Any number can be represented as the sum of 4 perfect squares
    2. Lagrange's Four Square theorem
    Result is 4 iff n can be written in the form 4^k*(8*m+7)
    """
    if is_perfect_sq(n):
        return 1

    while n % 4 == 0:
        n >>= 2
    if n % 8 == 7:
        return 4

    for a in range(math.ceil(math.sqrt(n))):
        b = n - a * a
        if is_perfect_sq(b):
            return 2

    return 3
