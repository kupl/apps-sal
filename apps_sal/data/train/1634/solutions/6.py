def total_inc_dec(x):
    if x < 3:
        return 1 if x < 1 else 10**x
    a = list(reversed(range(1, 10)))
    b = list(reversed(range(1, 11)))
    ttl = 10 * (2 - x)
    for _ in range(x - 1):
        p, q = a[0], b[0] = sum(a), sum(b)
        for i in range(1, 9):
            a[i], b[i] = sum(a[i:]), sum(b[i:])
        ttl += p + q
    return ttl
