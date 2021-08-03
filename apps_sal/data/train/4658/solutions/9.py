def max_product(lst, n_largest_elements):
    p = 1
    for x in sorted(lst, reverse=True)[:n_largest_elements]:
        p *= x
    return p
