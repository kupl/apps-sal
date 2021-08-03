def max_product(l, n):
    l = sorted(l)[::-1]
    res = 1
    for i in range(n):
        res *= l[i]
    return res
