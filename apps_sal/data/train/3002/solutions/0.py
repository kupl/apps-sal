import math


def is_pronic(n):
    return n >= 0 and math.sqrt(1 + 4 * n) % 1 == 0
