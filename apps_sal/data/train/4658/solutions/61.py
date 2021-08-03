def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    m = 1
    for a in range(n_largest_elements):
        m *= lst[a]
    return m
