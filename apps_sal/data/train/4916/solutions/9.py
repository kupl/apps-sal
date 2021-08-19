import itertools


def prime(a):
    return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))


def get_primes(how_many, group_size=2):
    primes = filter(prime, itertools.count(2))
    yield from itertools.zip_longest(*[itertools.islice(primes, how_many)] * group_size)
