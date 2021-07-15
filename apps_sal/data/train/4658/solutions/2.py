def max_product(lst, n_largest_elements):
    sorted_lst = sorted(lst, reverse=True)
    product = 1
    for i in range(n_largest_elements): product *= sorted_lst[i]
    return product
