def halving_sum(n):
    sum = 0
    exp = 0
    while n // 2 ** exp:
        sum += n // 2 ** exp
        exp += 1
    return sum
