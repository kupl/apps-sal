def halving_sum(n):
    res = n
    while n != 1:
        n = n // 2
        res += n
    return res
