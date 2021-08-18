def halving_sum(n):
    re = n
    while n > 1:
        n = n // 2
        re += n
    return re
