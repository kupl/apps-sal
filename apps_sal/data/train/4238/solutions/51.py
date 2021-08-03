import math


def squares_needed(n):
    if n == 0:
        return 0
    return int(math.log(n, 2) + 1)
