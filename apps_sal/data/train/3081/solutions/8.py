from random import randint


def squares(n):
    return [i ** 2 for i in range(1, n + 1)]


def num_range(n, start, step):
    return [start + i * step for i in range(n)]


def rand_range(n, mn, mx):
    return [randint(mn, mx) for i in range(n)]


def primes(n):
    def gen_prime(arr):
        yield arr[0]
        yield from gen_prime([i for i in arr if i % arr[0] != 0])
    primes = gen_prime(range(2, n**3))
    return [next(primes) for i in range(n)]
