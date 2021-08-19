LIMIT = 10 ** 6
sieve = [0] * 2 + list(range(2, LIMIT))
for n in sieve:
    if n:
        for i in range(n * n, LIMIT, n):
            sieve[i] = 0
PRIMES = list((n for n in sieve if n))


def get_primes(n, m=2):
    primes_ = PRIMES[:n] + [None] * m
    return (tuple(primes_[i:i + m]) for i in range(0, n, m))
