import math


def is_pronic(n):
    if n < 0:
        return False
    a = int(math.sqrt(n))
    return a * (a + 1) == n
