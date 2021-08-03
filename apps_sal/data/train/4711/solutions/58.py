from math import log


def zeros(n):
    if n == 0:
        return 0
    y = 0
    for x in range(1, int(log(n, 5) + 1)):
        y += n // (5**x)
    return y
