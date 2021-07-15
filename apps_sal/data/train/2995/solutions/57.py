def sum_mul(n, m):
    if n < 1 or m < 1:
        return'INVALID'
    s = 0
    x = n
    while x < m:
        s += x
        x += n
    else:
        return s
        return 0
