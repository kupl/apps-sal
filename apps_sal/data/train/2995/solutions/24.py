def sum_mul(n, m):
    return sum(el for el in range(n, m, n)) if n > 0 < m else 'INVALID'
