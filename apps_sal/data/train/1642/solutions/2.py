from math import gcd, factorial
from random import randint


def primesfrom2to(n):
    """
    Returns an array of primes, 2 <= p < n.
    """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


bound = 7100
small_primes = primesfrom2to(bound)
small_primes_set = set(small_primes)


def factorint(n):
    """
    Returns a dict containing the prime factors of n as keys and their
    respective multiplicities as values.
    """
    factors = dict()
    limit = int(n ** 0.5) + 1
    for prime in small_primes:
        if prime > limit:
            break
        while n % prime == 0:
            if prime in factors:
                factors[prime] += 1
            else:
                factors[prime] = 1
            n //= prime
    if n >= 2:
        large_factors(n, factors)
    return factors


def large_factors(n, factors):
    while n > 1:
        if isprime(n):
            if n in factors:
                factors[n] += 1
            else:
                factors[n] = 1
            break
        factor = pollard_brent(n)
        large_factors(factor, factors)
        n //= factor


def pollard_brent(n):
    """
    Returns a factor of n. The returned factor may be a composite number.
    """
    if n % 2 == 0:
        return 2
    (y, c, m) = (randint(1, n - 1), randint(1, n - 1), randint(1, n - 1))
    (g, r, q) = (1, 1, 1)
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x - y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break
    return g


def isprime(n):
    if n % 2 == 0:
        return False
    elif n < bound:
        return n in small_primes_set
    (d, r) = (n - 1, 0)
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def partitions(n, k):
    """
    Returns the number of ways to write n as the sum of k nonnegative 
    integers. Order matters.
    """
    result = 1
    for i in range(n + 1, n + k):
        result *= i
    return result // factorial(k - 1)


def multiply(n, k):
    (total, factors) = (1, factorint(n))
    for exponent in list(factors.values()):
        total *= partitions(exponent, k)
    return total
