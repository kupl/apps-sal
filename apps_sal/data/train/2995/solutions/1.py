def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'
