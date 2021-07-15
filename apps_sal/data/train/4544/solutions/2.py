def prime_factors(n):
    factors = []
    for k in (2, 3):
        while n % k == 0:
            n //= k
            factors.append(k)
    k = 5
    step = 2
    while k * k <= n:
        if n % k:
            k += step
            step = 6 - step
        else:
            n //= k
            factors.append(k)
    if n > 1:
        factors.append(n)
    return factors


def factor_sum(n):
    while True:
        fs = sum(prime_factors(n))
        if fs == n:
            return fs
        n = fs
