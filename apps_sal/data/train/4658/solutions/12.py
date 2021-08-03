def max_product(lst, n_largest_elements):
    l = sorted(lst, reverse=True)
    result = l[0]
    for i in range(1, n_largest_elements):
        result *= l[i]
    return result
