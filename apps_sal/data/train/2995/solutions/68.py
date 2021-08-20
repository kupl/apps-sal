def sum_mul(n, m):
    sum = 0
    inc = n
    if n > 0 and m > 0:
        while n < m:
            sum += n
            n += inc
        return sum
    else:
        return 'INVALID'
