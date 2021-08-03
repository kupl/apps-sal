def adjacent_element_product(array):
    res = array[0] * array[1]
    for i in range(2, len(array)):
        prod = array[i] * array[i - 1]
        if prod > res:
            res = prod
    return res
