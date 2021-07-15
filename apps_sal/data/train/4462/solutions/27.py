def adjacent_element_product(array):
    return max([i * l for i, l in zip(array, array[1:])])
