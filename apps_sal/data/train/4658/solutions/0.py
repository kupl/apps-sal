def max_product(lst, n_largest_elements):
    lst_largest = sorted(lst)[-n_largest_elements:]
    prod = 1
    for number in lst_largest:
        prod *= number
    return prod
