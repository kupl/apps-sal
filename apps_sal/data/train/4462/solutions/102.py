def adjacent_element_product(array):
    res = min(array) * max(array)
    for (i, item) in enumerate(array):
        if i + 1 < len(array):
            if item * array[i + 1] >= res:
                res = item * array[i + 1]
    return res
