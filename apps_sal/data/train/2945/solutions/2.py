import math


def fortune(f0, p, c0, n, i):
    f0 = math.trunc(f0 * (1 + p / 100) - c0)
    c0 = c0 * (1 + i / 100)
    if n == 2:
        return True if f0 >= 0 else False
    else:
        return fortune(f0, p, c0, n - 1, i)
