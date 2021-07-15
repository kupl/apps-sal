from itertools import combinations_with_replacement as replacements


primes = {2}
sieve = [True] * 5000
for i in range(3, 102, 2):
    if sieve[i // 2]:
        sieve[i * i // 2 :: i] = [False] * ((10001 - i * i - 1) // (2 * i) + 1)
primes.update((2 * i + 1) for i in range(1, 5000) if sieve[i])


def solve(a, b):
    pairs = replacements(set(range(a, b)) & primes, 2)
    return sum(1 for p, q in pairs if sum(int(d) for d in str(p * q)) in primes)

