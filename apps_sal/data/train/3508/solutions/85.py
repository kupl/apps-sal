def halving_sum(n):
    c = 0
    while n >= 1:
        c = c + n
        n = n // 2
    return c
