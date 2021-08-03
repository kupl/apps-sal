def halving_sum(n):
    summa = 0
    while n != 1:
        summa += n
        n = n // 2
    return summa + 1
