def max_product(lst, n_largest_elements):
    a = sorted(lst)[-n_largest_elements:]
    prod = 1
    for i in a:
        prod = prod * i
    return prod

