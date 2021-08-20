def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    if n == m or n > m:
        return 0
    if m % n == 0:
        return sum((n * i for i in range(1, m // n)))
    else:
        return sum((n * i for i in range(1, m // n + 1)))
