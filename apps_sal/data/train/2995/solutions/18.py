def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    else:
        return sum([i for i in range(1, m) if i % n == 0])
