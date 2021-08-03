from math import log2, ceil


def score(n):
    return n if n in (0, 1) else 2 ** (ceil(log2(n))) - 1
