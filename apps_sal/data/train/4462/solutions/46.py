def adjacent_element_product(array):
    max_product = array[0] * array[1]
    for i in range(len(array) - 1):
        subset = array[i] * array[i + 1]
        if subset > max_product:
            max_product = subset
    return max_product
