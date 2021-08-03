def halving_sum(n):
    summed = 0
    x = 1
    while n // x > 0:
        summed += n // x
        x *= 2

    return summed
