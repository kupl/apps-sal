def halving_sum(n):
    m = n
    summ = 0
    count = 1
    while n // count >= 1:
        summ += n // count
        count *= 2
    return summ
