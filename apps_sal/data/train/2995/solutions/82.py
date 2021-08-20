def sum_mul(n, m):
    print((n, m))
    return sum(range(n, m, n)) if n != 0 and m > 0 and (n > 0) else 'INVALID'
