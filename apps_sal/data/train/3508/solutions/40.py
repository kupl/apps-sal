def halving_sum(n):
    tot = 0
    while n != 1:
        tot += n
        n = n // 2
    return tot + 1
