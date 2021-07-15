def max_product(lst, n_largest_elements):
    lst = sorted(lst)
    product = 1
    for i in range(n_largest_elements):
        product *= lst[-i-1]
    return product
