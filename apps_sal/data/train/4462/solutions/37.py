def adjacent_element_product(array):
    maxProduct = array[0] * array[1]
    for i in range(1, len(array) - 1):
        product = array[i] * array[i + 1]
        if product > maxProduct:
            maxProduct = product

    return maxProduct
