def sum_mul(n, m):
    if m < 1 or n < 1:
        return 'INVALID'
    return 0 if m < n else n * sum(range(1 + (m - 1) // n))
