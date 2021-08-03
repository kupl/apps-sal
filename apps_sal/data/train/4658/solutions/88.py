def max_product(lst, n_largest_elements):
    a = sorted(lst)
    c = 1
    for i in a[-n_largest_elements::]:
        c = c * i
    return c
