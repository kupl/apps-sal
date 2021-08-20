from bisect import bisect
from itertools import product


def is_prime(n):
    return n % 2 and all((n % x for x in range(3, int(n ** 0.5) + 1, 2)))


prime_digits = (int(''.join(p)) for k in range(2, 6) for p in product('2357', repeat=k))
non_primes = [n for n in prime_digits if not is_prime(n)]


def not_primes(a, b):
    return non_primes[bisect(non_primes, a - 1):bisect(non_primes, b - 1)]
