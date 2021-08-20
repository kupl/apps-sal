def max_product(lst, n_largest_elements):
    x = sorted(lst)[-n_largest_elements:]
    p = 1
    for i in x:
        p *= i
    return p
