def max_product(lst, n_largest_elements):
    sorted_list = sorted(lst, reverse=True)
    list = sorted_list[:n_largest_elements]
    res = 1
    for i in list:
        res = res * i
    return res
