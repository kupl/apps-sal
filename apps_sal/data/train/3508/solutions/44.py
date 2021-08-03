def halving_sum(n):
    hold = 0
    x = 1
    while n // x > 0:
        hold += n // x
        x *= 2
    return hold
