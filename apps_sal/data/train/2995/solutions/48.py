def sum_mul(n, m):
    if (n<=0)+(m<=0): return 'INVALID'
    return sum([i for i in range(n, m, n)])
