def sum_mul(n, m):
    if n == 0:
        return 'INVALID'
    elif m <= 0 or n < 0:
        return 'INVALID'
    elif n > m:
        return 0
    elif m > n:
        return sum(range(n, m, n))
    elif n == m or n > m:
        return 0

