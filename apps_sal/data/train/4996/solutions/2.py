from itertools import islice


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def fibs_fizz_buzz(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in islice(fib(), n)]
