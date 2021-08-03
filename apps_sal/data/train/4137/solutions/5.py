import math


def is_square(n):
    return n >= 0 and int(math.sqrt(n)) ** 2 == n
