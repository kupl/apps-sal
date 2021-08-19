from itertools import chain
from functools import reduce


def factors(n):
    return set(chain.from_iterable(([d, n // d] for d in range(1, int(n ** 0.5) + 1) if n % d == 0)))


def square_factors(n):
    return reduce(lambda s, d: s + d ** 2, factors(n), 0)


def list_squared(m, n):
    l = []
    for x in range(m, n + 1):
        s = square_factors(x)
        if (s ** 0.5).is_integer():
            l.append([x, s])
    return l
