def sum_mul(n, m):
    if n == m and n != 0:
        return 0
    elif n > 0 and m > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
