def max_product(lst, n_largest_elements):
    lst = sorted(lst)[::-1]
    c = 1
    for i in range(n_largest_elements):
        c = c * lst[i]
    return c
