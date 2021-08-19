def sum_mul(n, m):
    if n < 0 and m > 0 or (m < 0 and n > 0):
        return 'INVALID'
    elif n == 0 and n == 0 or (m == 0 or n == 0):
        return 'INVALID'
    else:
        return sum(range(n, m, n))
