def S2N(m, n):
    return sum(b ** e for b in range(m + 1) for e in range(n + 1))
