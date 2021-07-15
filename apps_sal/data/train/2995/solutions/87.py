def sum_mul(n, m):
    sum_n = 'INVALID'
    if n > 0 and m > 0:
        num = (m - 1) // n
        sum_n = (n * num * (num + 1)) // 2
    return sum_n
