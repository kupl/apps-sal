from bisect import bisect
n = 10 ** 6
(dominant, primes, sieve) = ([], set(), [0, 0] + [1] * (n - 2))
for k in range(n):
    if sieve[k]:
        primes.add(k)
        sieve[k * k::k] = ((n - k * k - 1) // k + 1) * [0]
        if len(primes) in primes:
            dominant.append(k)


def solve(a, b):
    return sum(dominant[bisect(dominant, a - 1):bisect(dominant, b)])
