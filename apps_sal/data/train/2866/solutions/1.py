def mobius(n):
    s, p, m = 0, 2, n ** .5
    while p <= m:
        if not n % p:
            s += 1
            n //= p
        if not n % p:
            return 0
        p += 1
    if n > 1:
        s += 1
    return 1 - s % 2 * 2
