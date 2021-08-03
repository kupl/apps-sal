def sum_mul(n, m):
    return 'INVALID' if n < 1 or m < 1 else sum([x for x in range(n, m, n)])
