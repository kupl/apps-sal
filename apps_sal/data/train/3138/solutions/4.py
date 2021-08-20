from math import log
from collections import deque


def climb(n):
    return [n // 2 ** i for i in range(int(log(n, 2)) + 1)][::-1]


def climb(n):
    """This is much faster."""
    seq = deque([n])
    while n > 1:
        n //= 2
        seq.appendleft(n)
    return list(seq)
