def adjacent_element_product(array):
    M = array[0] * array[1]
    for i, element in enumerate(array[1:]):
        x = element * array[i]
        if x > M:
            M = x
    return M
