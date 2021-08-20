import math


def halving_sum(n):
    return 1 if n == 1 else sum([math.floor(n / 2 ** i) for i in range(0, math.floor(n / 2)) if math.floor(n / 2 ** i) >= 1])
