def halving_sum(n):
    sm = 0
    while n > 0:
        sm += n
        n //= 2
    return sm
