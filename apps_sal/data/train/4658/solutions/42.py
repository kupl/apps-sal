def max_product(lst, n_largest_elements):
    lst = sorted(lst, reverse=True)[0:n_largest_elements]
    n = 1
    for x in range(n_largest_elements):
        n *= lst[x]
    return n

