def f(n):
    (p, n_, m) = (2, 1, int(n ** 0.5))
    while n > 1 and p <= m:
        k = 0
        while not n % p:
            k += 1
            n //= p
        if k:
            n_ *= k * p ** (k - 1)
        p += 1
    return n_
