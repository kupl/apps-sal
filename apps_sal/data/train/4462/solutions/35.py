def adjacent_element_product(array):
    m = None
    for i in range(1, len(array)):
        if m == None or array[i] * array[i - 1] > m:
            m = array[i] * array[i - 1]
    return m
