from itertools import count


def isPrime(n): return n == 2 or all(n % x for x in range(3, int(n**.5 + 1), 2))


def prime_bef_aft(n):
    delta = 2 - (n % 2 == 0)
    return [next(v + (v == 1) for v in count(n - delta, -2) if isPrime(v) or v == 1),
            next(v for v in count(n + delta, 2) if isPrime(v))]
