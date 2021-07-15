def adjacent_element_product(array):
    return max(map(lambda i: array[i] * array[i + 1], range(len(array) - 1)))
