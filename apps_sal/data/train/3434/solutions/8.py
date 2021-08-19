def bin_mul(m, n):
    r = []
    (n, m) = sorted([m, n])
    if n == 0:
        return []
    while m > 1:
        if m % 2 == 1:
            r.insert(0, n)
        m //= 2
        n *= 2
    r.insert(0, n)
    return r
