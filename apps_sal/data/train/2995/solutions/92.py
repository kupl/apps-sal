def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    sum = 0
    for i in range(1, m):
        if i * n < m:
            sum += i * n
    return sum
    pass
