def max_product(lst, n_largest_elements):
    lst.sort()
    c = 1
    for i in lst[-n_largest_elements:]:
        c = i * c
    return c
