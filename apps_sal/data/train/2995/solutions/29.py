def sum_mul(n, m):
    # it is invalid if n or m is less or equal to zero
    return 'INVALID' if n <= 0 or m <= 0 else sum([i for i in range(n, m, n)])
