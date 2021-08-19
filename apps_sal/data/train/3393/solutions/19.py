from math import ceil
from functools import lru_cache


def find_square_sums(m, n):
    for x in range(m, n + 1):
        c = candidate(x)
        if c:
            yield c


def candidate(n):
    total = sum((x ** 2 for x in divisors(n)))
    if (total ** 0.5).is_integer():
        return [n, total]
    return False


@lru_cache(maxsize=100000)
def divisors(n):
    divs = [1, n]
    for x in range(2, ceil((n + 1) / 2)):
        if x in divs:
            break
        if n % x == 0:
            divs.append(x)
            divs.append(int(n / x))
    return set(divs)


def list_squared(m, n):
    return list(find_square_sums(m, n))
