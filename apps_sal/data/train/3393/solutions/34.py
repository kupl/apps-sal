def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def factorize(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i > 0:
            factors.append((p, i))
    if n > 1:
        factors.append((n, 1))
    return factors


def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p ** e for d in div for e in range(r + 1)]
    return div


def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        sum_i = 0
        for d in divisors(factorize(i, gen_primes())):
            sum_i += d * d
        if is_sqrt(sum_i):
            result.append([i, sum_i])
    return result


def is_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x * x == n
