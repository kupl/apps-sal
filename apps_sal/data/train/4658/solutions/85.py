def max_product(lst, n_largest_elements):
    lst.sort()
    product = 1

    for i in lst[len(lst) - n_largest_elements:]:
        product *= i

    return product
