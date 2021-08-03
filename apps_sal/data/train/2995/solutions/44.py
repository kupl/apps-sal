def sum_mul(n, m):
    return sum(i for i in range(0, m, n)) if 0 < n and 0 < m else "INVALID"
