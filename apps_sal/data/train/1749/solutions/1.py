from collections import defaultdict


def pf(n):
    primes = defaultdict(lambda: 0)
    i = 2
    while n > 1 and i * i <= n:
        if n % i == 0:
            while n % i == 0:
                primes[i] = primes[i] + 1
                n /= i
        i += 1
    if n > 1:
        primes[n] = primes[n] + 1
    return primes


def reduce(n, p): return 0 if n < p else n // p + reduce(n // p, p)


def trailing_zeros(num, base):
    mx = float('inf')
    primes = pf(base)
    for p in primes:
        mx = min(mx, reduce(num, p) // primes[p])
    return mx
