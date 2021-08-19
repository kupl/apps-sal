def adjacent_element_product(array):
    max = -99999999999
    for (i, n) in enumerate(array):
        if i < len(array) - 1 and n * array[i + 1] > max:
            max = n * array[i + 1]
    return max
