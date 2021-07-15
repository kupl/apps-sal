from math import floor
def next_perfect_square(n):
    return (floor(n**(1/2)) + 1) ** 2 if n > 0 else 0 if n != 0 else 1
