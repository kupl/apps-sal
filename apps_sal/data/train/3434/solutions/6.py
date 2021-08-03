def bin_mul(m, n):
    n, m = sorted((m, n))
    r = [n] if (m % 2 and n) else []
    while m:
        m >>= 1
        n <<= 1
        if m % 2 and n:
            r.append(n)
    return sorted(r, reverse=True)
