def step(g, m, n):
    return next(([a, a + g] for a in range(m, n - g + 1) if is_prime(a) and is_prime(a + g)), None)


def is_prime(n):
    factors = 0
    for k in (2, 3):
        while n % k == 0 and factors < 2:
            n //= k
            factors += 1
    k = 5
    step = 2
    while k * k <= n and factors < 2:
        if n % k:
            k += step
            step = 6 - step
        else:
            n //= k
            factors += 1
    if n > 1:
        factors += 1
    return factors == 1
