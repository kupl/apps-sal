def adjacent_element_product(array):
    max_prod = max([i * array[_index + 1] for (_index, i) in enumerate(array[:-1])])
    return max_prod
