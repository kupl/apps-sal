def halving_sum(n):
    total_sum = n

    while n != 1:
        n = n // 2
        total_sum += n

    return total_sum
