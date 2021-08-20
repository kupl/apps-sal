import math


def halving_sum(n):
    return sum((n // 2 ** x for x in range(int(math.log2(n)) + 1)))
