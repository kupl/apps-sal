import math


def next_perfect_square(n):
    return math.ceil((n + 1) ** 0.5) ** 2 if n > -1 else 0
