def sum_mul(n, m):
    return 0 if m == n else "INVALID" if n <= 0 or m <= 0 else sum(range(n, m, n))
