def halving_sum(n):
    res = n
    while n != 1:
        n = int(n / 2)
        res += n

    return res
