from math import log2
from collections import Counter


def largest_power(n):
    if n == 1:
        return (0, -1)
    return (1, -1) if n < 5 else max(Counter((int(round((n - 1) ** (1 / p), 12)) ** p for p in range(2, int(log2(n - 1)) + 1))).items(), key=lambda p: p[0])
