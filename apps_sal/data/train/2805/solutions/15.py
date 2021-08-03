from itertools import dropwhile


def fib_gen():
    a, b = 0, 1
    while True:
        yield a, b
        a, b = b, a + b


def productFib(p):
    i = dropwhile(lambda x: x[0] * x[1] < p, fib_gen())
    a, b = next(i)

    return [a, b, a * b == p]
