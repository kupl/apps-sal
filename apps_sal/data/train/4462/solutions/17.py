def adjacent_element_product(array): return max([a * b for a, b in zip(array[:-1], array[1:])])
