def halving_sum(n):
    add = n
    while n > 1:
        n = n // 2
        add += n
    return add
