from math import factorial as fact
from fractions import Fraction


def comb(n, k):
    return fact(n) // fact(k) // fact(n - k)


result = {0: 1, 1: Fraction(-1, 2), 2: Fraction(1, 6)}


def bernoulli_number(n):
    if n in result or n & 1:
        return result.get(n, 0)
    for x in range(max(result) + 2, n + 1, 2):
        result[x] = -Fraction(sum((comb(x + 1, k) * result.get(k, 0) for k in range(x))), comb(x + 1, x))
    return result[n]
