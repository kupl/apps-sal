from itertools import product
LIMIT = 10 ** 5
primes = set((n for n in range(3, LIMIT, 2) if all((n % x for x in range(3, int(n ** 0.5) + 1, 2)))))
(non_primes, digits, n) = ([], ['14689'], 0)
while n < LIMIT:
    for n in product(*digits):
        n = int(''.join(n))
        if n not in primes:
            non_primes.append(n)
    digits.append('014689')


def solve(n):
    return non_primes[n]
