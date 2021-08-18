def sum_mul(n, m):
    return 'INVALID' if n <= 0 or m <= 0 else sum([i for i in range(n, m, n)])
