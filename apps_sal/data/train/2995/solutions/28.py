def sum_mul(n, m):
    print((n, m))
    if m <= 0 or n <= 0:
        return 'INVALID'
    return sum(range(n, m, n))

