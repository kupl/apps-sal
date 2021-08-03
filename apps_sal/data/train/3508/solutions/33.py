import math


def halving_sum(n):
    return sum([n // 2 ** i for i in range(math.ceil(math.log(n, 2)))]) if n > 1 else 1
