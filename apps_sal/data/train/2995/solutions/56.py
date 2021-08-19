def sum_mul(n, m):
    ctr = 0
    if m <= 0 or n <= 0:
        return 'INVALID'
    for i in range(1, m):
        if i % n == 0:
            ctr += i
    return ctr
