from math import sqrt


def primes_a_p(lower_limit, upper_limit):
    primes = [p for p in prime_sieve(upper_limit + 1) if p >= lower_limit]
    res = []
    for k in range(30, upper_limit // 5, 30):
        terms = [0, k, 2 * k, 3 * k, 4 * k, 5 * k]
        for p in primes:
            pp = [t + p for t in terms]
            if all((t in primes for t in pp)):
                res.append(pp)
    return sorted(res, key=lambda v: v[0])


def prime_sieve(n):
    sieve = [True] * n
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
