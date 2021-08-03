def max_product(lst, n_largest_elements):
    a = sorted(lst, reverse=True)
    b = 1
    for i in range(n_largest_elements):
        b *= a[i]
    return b
