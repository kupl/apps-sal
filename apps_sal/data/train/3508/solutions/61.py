def halving_sum(n):
    sum = 0
    if n >= 1:
        sum += n + halving_sum(n // 2)
    return sum
