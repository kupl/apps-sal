def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if n and n > 0 and m > 0 else 'INVALID'
