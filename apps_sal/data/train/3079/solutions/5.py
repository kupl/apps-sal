def big_primefac_div(n):
    if n % 1:
        return 'The number has a decimal part. No Results'
    n = abs(int(n))
    mpf = big_primefac(n)
    return [mpf, big_div(n)] if mpf != n else []


def big_primefac(n):
    m = 1
    while n % 2 == 0:
        (m, n) = (2, n // 2)
    k = 3
    while k * k <= n:
        if n % k:
            k = k + 2
        else:
            (m, n) = (k, n // k)
    return max(m, n)


def big_div(n):
    return next((n // k for k in range(2, int(n ** 0.5) + 1) if n % k == 0), n)
