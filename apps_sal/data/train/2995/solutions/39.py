def sum_mul(n, m):
    if n == 0 or m <= 0 or n <= 0:
        return 'INVALID'
    return sum([n * i for i in range(1, m) if n * i < m])
