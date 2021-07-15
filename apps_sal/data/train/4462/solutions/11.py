def adjacent_element_product(array):
    max_product = array[0] * array[1]
    i = 2
    while i < len(array):
        max_product = max(max_product, array[i-1]*array[i])
        i += 1
    return max_product
