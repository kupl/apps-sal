def sum_mul(n, m):
    s = 0
    if m <= 0 or n <= 0:
        return 'INVALID'
    else:
        i = 1
        while i * n < m:
            s += i * n
            i += 1
    return s
