def adjacent_element_product(array):
    m = -1000000
    for i in range(len(array) - 1):
        m = max(m, array[i] * array[i + 1])

    return m
