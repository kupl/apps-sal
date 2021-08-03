def max_multiple(divisor, bound):
    iter = 1
    lst = []
    mul = 1
    while mul <= bound:
        mul = iter * divisor
        lst.append(mul)
        iter += 1
    return lst[-2]
