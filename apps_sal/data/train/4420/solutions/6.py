def prime_factorizations(n):
    sieve = [0 for x in range(n)]
    for i in range(2, n):
        if not sieve[i]:
            sieve[i] = i
            for r in range(i, n, i):
                sieve[r] = sieve[r] or i
    return sieve


def factor_sum(sieve, n):
    results = 0
    while n > 1:
        p = sieve[n]
        results += p
        if p == n:
            break
        n //= p
    return results


def mult_primefactor_sum(a, b):
    sieve = prime_factorizations(b + 1)
    return [n for n in range(a, b + 1) if sieve[n] != n and n % factor_sum(sieve, n) == 0]
