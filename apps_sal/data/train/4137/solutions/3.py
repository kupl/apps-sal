import math


def is_square(n):
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False
