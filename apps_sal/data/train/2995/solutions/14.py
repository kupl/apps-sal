def sum_mul(n, m):
    if n > 0 and m > 0:
        k = max(m // n - (not m % n), 0)
        return n * k * (k + 1) // 2
    return 'INVALID'
