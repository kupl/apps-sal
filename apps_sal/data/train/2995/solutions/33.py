def sum_mul(n, m):
    if n < 1 or m < 1:
        return 'INVALID'
    else:
        return sum((n * i for i in range(m // n + 1))) if m % n != 0 else sum((n * i for i in range(m // n)))
    (2, 4, 6, 8)
