from itertools import count
from math import log


def decompose(n):
    r = []
    for x in count(2):
        if x > n:
            break
        m = int(log(n, x))
        if m == 1:
            break
        r.append(m)
        n -= x ** m
    return [r, n]
