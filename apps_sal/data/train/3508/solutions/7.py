def halving_sum(n):
    r = 0
    while n:
        r += n
        n >>= 1
    return r
