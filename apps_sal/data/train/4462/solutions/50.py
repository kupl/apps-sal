def adjacent_element_product(array):
    return max(list(map(lambda x, y: x * y, array[:-1], array[1:])))
