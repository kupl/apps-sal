def sum_mul(n, m):
    if m <= 0 or n <=0:
        return 'INVALID'
    return sum([i for i in range(n,m+1) if i % n == 0 and i < m])

