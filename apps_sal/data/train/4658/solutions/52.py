def max_product(lst, n_largest_elements):
    l = sorted(lst, reverse=True)
    res = 1
    for i in range(0, n_largest_elements):
        res *= l[i]
    return res
