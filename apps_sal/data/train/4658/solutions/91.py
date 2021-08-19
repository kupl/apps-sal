def max_product(lst, n_largest_elements):
    prod = 1
    for i in sorted(lst)[-n_largest_elements:]:
        prod *= i
    return prod
