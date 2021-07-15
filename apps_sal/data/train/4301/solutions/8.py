def calc_ms(n):
    res = 1
    while n > 0:
        res *= 20
        n -= 1
    return res
