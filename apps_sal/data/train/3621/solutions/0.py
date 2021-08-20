LIMIT = 500000
sieve = [True] * (LIMIT // 2)
for n in range(3, int(LIMIT ** 0.5) + 1, 2):
    if sieve[n // 2]:
        sieve[n * n // 2::n] = [False] * ((LIMIT - n * n - 1) // 2 // n + 1)
PRIMES = [2] + [2 * i + 1 for i in range(1, LIMIT // 2) if sieve[i]]


def prime_maxlength_chain(val_max):
    if val_max < 5:
        return []
    found = []
    for n in range(2, 400):
        if sum(PRIMES[:n]) >= val_max:
            max_size = n
            break
    for size in range(max_size, 1, -1):
        if size % 2 == 0:
            n = sum(PRIMES[:size])
            if n < val_max and n in PRIMES:
                return [n]
        else:
            for start in range(1, max_size - size + 1):
                n = sum(PRIMES[start:start + size])
                if n < val_max and n in PRIMES:
                    found.append(n)
            if found:
                return found
