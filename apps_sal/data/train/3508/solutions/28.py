def halving_sum(n):
    cnt = 2
    s = n

    while n // cnt > 0:
        s += n // cnt
        cnt *= 2

    return s
