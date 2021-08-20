from itertools import islice
from math import factorial


def fib():
    (a, b) = (0, 1)
    while True:
        yield a
        (a, b) = (b, a + b)


def sum_fib(n):
    return sum(map(factorial, islice(fib(), n)))
