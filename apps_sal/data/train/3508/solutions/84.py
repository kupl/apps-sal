def halving_sum(n):
    res = 0
    while n > 1:
        res = res + n
        n = n // 2
    return res + 1
