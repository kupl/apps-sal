import math


def zeros(n):
    return 0 if n < 2 else sum([n // (5**f) for f in range(1, max(2, int(math.log(n)))) if 5**f <= n])
