def max_multiple(divisor, bound):
    res = 0
    for i in range(bound + 1):
        if i % divisor == 0:
            if i > res:
                res = i
    return res
