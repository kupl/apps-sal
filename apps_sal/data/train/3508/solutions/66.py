def halving_sum(n):
    running_total = 0
    while (n > 0):
        running_total += n
        n = n // 2
    return running_total
