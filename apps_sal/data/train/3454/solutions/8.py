from operator import mul
from functools import reduce


def candies_to_buy(n):
    ret = []
    for i in range(1, n + 1):
        s = i
        for j in ret:
            if s % j == 0:
                s //= j
            if s == 1:
                break
        ret.append(s)
    return reduce(mul, ret)
