def sum_mul(n, m):
    sumu = 0
    if n > 0 and m > 0:
        for i in range(n, m):
            if i % n == 0:
                sumu += i
    else:
        return 'INVALID'
    return sumu
