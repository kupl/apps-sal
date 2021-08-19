from operator import mul
from functools import reduce, partial
from itertools import combinations


def prod(numbers):
    return reduce(mul, numbers)


def range_sum(n):
    return n * (n + 1) / 2


def multipes_sum(divisor, n):
    return range_sum(n // divisor) * divisor


def something(limit, divisors, size):
    """How should I name this?"""
    return sum((multipes_sum(prod(numbers), limit) for numbers in combinations(divisors, size)))


def divisors_multiples_sum(n, divisors=()):
    result = 0
    for i in range(len(divisors)):
        result += (-1) ** i * something(n, divisors, i + 1)
    return int(result)


find = partial(divisors_multiples_sum, divisors=(3, 5))
