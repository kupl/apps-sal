from random import randint
PRIMES = [2] + [n for n in range(3, 10 ** 3, 2) if all((n % d for d in range(3, int(n ** 0.5) + 1, 2)))]


def squares(n):
    return [x * x for x in range(1, n + 1)]


def num_range(n, start, step):
    return [start + step * i for i in range(n)]


def rand_range(n, mn, mx):
    return [randint(mn, mx) for _ in range(n)]


def primes(n):
    return PRIMES[:n]
