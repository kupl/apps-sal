from itertools import takewhile


def efib():
    a, b = 0, 1
    while True:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


def even_fib(m):
    return sum(takewhile(lambda x: x < m, efib()))
