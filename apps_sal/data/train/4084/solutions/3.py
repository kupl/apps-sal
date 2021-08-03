from math import log


def alex_mistakes(katas, limit):
    return int(log((limit - katas * 6 + 5) / 5, 2))
