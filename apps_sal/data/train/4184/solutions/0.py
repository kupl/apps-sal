primes = [2, 3, 5, 7]


def is_prime(n):
    if n < 2:
        return False
    m = int(n ** 0.5) + 1
    for p in primes:
        if p >= m:
            break
        if not n % p:
            return False
    (q, d) = (primes[-1], 4 if (n + 1) % 6 else 2)
    while q < m:
        (q, d) = (q + d, 4 - d)
        if is_prime(q):
            primes.append(q)
            if not n % q:
                return False
    return True
