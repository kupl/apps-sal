def halving_sum(n):
    sum = 0
    while n != 1:
        sum = sum + n
        n = n // 2
    return sum + 1
