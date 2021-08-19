import itertools
from fractions import Fraction as F
import functools


def convergents_of_e(n):
    print(n)

    for i in range(200, n, 200):
        h(cont_e_2, i)  # recursion depth error prevent by precalculating

    return sum_dig(h(cont_e_2, n - 1))


def sum_dig(n):
    return sum(map(int, str(n)))


def cont_e():
    for i in [2, 1, 2]:
        yield i
    for i in itertools.count(start=2):
        yield 1
        yield 1
        yield 2 * i


@functools.lru_cache(None)
def cont_e_2(n):
    if n == 0:
        return 2
    if n % 3 == 2:
        return ((n + 1) * 2) // 3
    return 1


@functools.lru_cache(maxsize=None)
def h(func, n):
    # source: https://en.wikipedia.org/wiki/Continued_fraction#Some_useful_theorems
    a = func(n)
    if n < 0:
        val = 2 + n
    else:
        val = a * h(func, n - 1) + h(func, n - 2)
    return val
