def sum_mul(n, m):
    return sum([i for i in range(m) if not i % n]) if m > 0 < n else 'INVALID'
