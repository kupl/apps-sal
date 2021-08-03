def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return ((m - 1) // n) * (1 + (m - 1) // n) * n // 2
