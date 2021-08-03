def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    p = (m - 1) // n
    return (n * p * (p + 1)) // 2
