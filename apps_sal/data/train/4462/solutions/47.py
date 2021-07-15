def adjacent_element_product(array):
    return max(i * array[idx - 1] for idx, i in enumerate(array[1:], 1))
