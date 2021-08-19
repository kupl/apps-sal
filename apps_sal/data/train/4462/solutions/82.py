def adjacent_element_product(array):
    return max((k * i for (i, k) in zip(array, array[1:])))
