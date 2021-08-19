def adjacent_element_product(array):
    m = array[0] * array[1]
    for i in range(1, len(array) - 1):
        m = max(m, array[i] * array[i + 1])
    return m
