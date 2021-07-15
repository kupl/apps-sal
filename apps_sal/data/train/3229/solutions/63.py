from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

@lru_cache(None)
def factorial_cache(n):
    if n == 0:
        return 1
    return n * factorial_cache(n - 1)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def am_i_wilson(n):
    print(n)
    try:
        return n > 0 and is_prime(n) and (factorial_cache(n - 1) + 1) % (n * n) == 0
    except:
        return False
