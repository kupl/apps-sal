from functools import reduce


def primes_sieve(n):
    sieve = [False, False] + [True] * (n - 1)
    limit = int(n ** 0.5) + 1
    for k in range(2, limit):
        if sieve[k]:
            i = k * 2
            l = (n - k) // k
            sieve[i::k] = [False] * l
    return [p for p, is_prime in enumerate(sieve) if is_prime]


primes = primes_sieve(8000)


def num_primorial(n):
    return reduce(int.__mul__, primes[:n])
