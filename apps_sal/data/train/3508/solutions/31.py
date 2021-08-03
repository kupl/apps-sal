def halving_sum(n):
    sum = 1
    while (n != 1):
        sum += n
        n = n // 2
    return (sum)
