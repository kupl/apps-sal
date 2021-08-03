def adjacent_element_product(array):
    return max([array[x] * array[x - 1] for x in range(1, len(array))])
