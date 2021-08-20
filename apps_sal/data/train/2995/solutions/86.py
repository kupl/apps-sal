def sum_mul(n, m):
    sum_n = 'INVALID'
    if n > 0 and m > 0:
        sum_n = sum(range(n, m, n))
    return sum_n
