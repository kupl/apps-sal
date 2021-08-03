from math import log


def alex_mistakes(n, time):
    return int(log((time - n * 6) / 5 + 1, 2))
