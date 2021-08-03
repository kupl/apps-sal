from math import log


def squares_needed(n):
    if not n:
        return 0
    return int(log(n + 0.0001, 2)) + 1
