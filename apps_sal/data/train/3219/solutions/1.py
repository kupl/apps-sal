n = 6005904
sieve = [True] * (n // 2)
for i in range(3, int(n ** 0.5) + 1, 2):
    if sieve[i // 2]:
        sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
primes = {2} | {2 * i + 1 for i in range(1, n // 2) if sieve[i]}


def find_primes_sextuplet(limit):
    i = limit // 6 - 8
    p = next((n for n in range(i, i + 10) if n % 10 == 7))
    while not {p, p + 4, p + 6, p + 10, p + 12, p + 16}.issubset(primes):
        p += 10
    return [p, p + 4, p + 6, p + 10, p + 12, p + 16]
