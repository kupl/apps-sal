from bisect import bisect


def prime_product(n):
    bisect_point = bisect(primes, n // 2)

    if n % 2:
        return 2 * (n - 2) if n - 2 in prime_set else 0

    for prime in primes[:bisect_point][::-1]:
        if n - prime in prime_set:
            return prime * (n - prime)

    return 0


def get_primes(n):
    """Sieve of Eratosthenes to calculate all primes less than or equal to n.

    Return set of primes.
    """
    primes = [True] * (n + 1)

    for num in range(2, int(n ** 0.5) + 1):
        if primes[num]:
            primes[num * 2::num] = [False] * len(primes[num * 2::num])

    return [i for i, x in enumerate(primes) if x and i > 1]


max_input = 100000
primes = get_primes(max_input)
prime_set = set(primes)
