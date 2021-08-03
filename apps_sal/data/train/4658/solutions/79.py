def max_product(lst, n):
    s = 1
    ls = sorted(lst, reverse=True)
    for i in ls[:n]:
        s *= i
    return s
