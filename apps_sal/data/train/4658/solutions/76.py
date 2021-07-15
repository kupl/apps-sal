def max_product(lst, n_largest_elements):
    arr = sorted(lst)[-n_largest_elements:]
    output = 1
    for elem in arr:
        output *= elem
    return output
