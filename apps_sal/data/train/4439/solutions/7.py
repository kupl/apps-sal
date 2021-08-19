from functools import lru_cache


@lru_cache(maxsize=None)
def count(n):
    x = n ** 0.5
    return 2 * sum((n % y == 0 for y in range(1, int(x + 1)))) - (x % 1 == 0)


def div_num(a, b):
    if a > b:
        return 'Error'
    return max(range(a, b + 1), key=count)
