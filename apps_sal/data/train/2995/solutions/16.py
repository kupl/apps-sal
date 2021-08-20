def sum_mul(n, m):
    return 'INVALID' if n <= 0 or m <= 0 else sum((x for x in range(m) if x % n == 0))
