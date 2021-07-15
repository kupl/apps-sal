def sum_mul(n, m):
    return sum([x for x in range(n, m, n)]) if n > 0 < m else "INVALID"
