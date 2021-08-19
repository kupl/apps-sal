LIMIT = 10 ** 6
primes = []
sieve = list(range(LIMIT))
sieve[1] = 0
for n in sieve:
    if n:
        primes.append(n)
        for i in range(n * n, LIMIT, n):
            sieve[i] = 0
Copeland_Erdos = ''.join(map(str, primes))


def solve(a, b):
    return Copeland_Erdos[a:a + b]
