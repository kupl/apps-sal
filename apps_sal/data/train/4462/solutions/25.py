def adjacent_element_product(array):
    m = -10000000
    for n, i in enumerate(array[:-1]):
        m = max(m, i * array[n + 1])

    return m
