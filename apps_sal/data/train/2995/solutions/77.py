def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    if m % n == 0:
        return sum((x * n for x in range(m // n)))
    return sum((x * n for x in range(m // n + 1)))
