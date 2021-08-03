def sum_mul(n, m):
    s = n > 0 and sum([i for i in range(n, m, n)])
    return ['INVALID', s][n > 0 and m > 0]
