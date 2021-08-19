from functools import reduce
from operator import mul
PRIMES = [2] + [x for x in range(3, 10 ** 4, 2) if all((x % d for d in range(3, int(x ** 0.5) + 1, 2)))]


def num_primorial(n):
    return reduce(mul, PRIMES[:n])
