def sum_mul(n, m):
    if n < 1 or m < 1:
        return 'INVALID'
    else:
        sum = 0
        for i in range(n, m, n):
            sum += i
        return sum
