import itertools
primes = [2] + [n for n in range(3, 1000, 2) if all((n % r for r in range(3, int(n ** 0.5) + 1, 2)))]


def prime_primes(N):
    pairs = list(itertools.combinations((p for p in primes if p < N), 2))
    return (len(pairs), int(sum((a / b for (a, b) in pairs))))
