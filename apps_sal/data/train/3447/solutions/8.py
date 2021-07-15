from math import sqrt

def next_perfect_square(n):
    return 0 if n < 0 else (int(sqrt(n)) + 1) ** 2
