from math import factorial, ceil, sqrt
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for x in range(2, ceil(sqrt(n))):
        if n % x == 0:
            return False
    return True


@lru_cache(maxsize=None)
def fact(n):
    return factorial(n)


def am_i_wilson(P):
    if not is_prime(P):
        return False

    if P - 1 <= 0:
        return False
    try:
        x = (fact(P - 1) + 1) % (P * P) == 0
        return x
    except OverflowError:
        return False
