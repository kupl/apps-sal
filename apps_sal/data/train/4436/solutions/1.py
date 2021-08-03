def S2N(m, n):
    return sum((a**(n + 1) - 1) // (a - 1) if a != 1 else n + 1 for a in range(m + 1))
