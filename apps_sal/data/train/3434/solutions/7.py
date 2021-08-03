def bin_mul(m, n):
    r = []
    n, m = sorted((m, n))
    if not n:
        return r
    while m:
        if m % 2:
            r += n,
        m //= 2
        n *= 2
    return r[::-1]
