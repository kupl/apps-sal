import math


def count(n):
    if n == 0 or n <= 1:
        return 1
    x = n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2
    return math.floor(x) + 1
