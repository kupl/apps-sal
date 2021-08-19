def adjacent_element_product(array):
    maximum = array[0] * array[1]
    for (n1, n2) in zip(array[1:], array[2:]):
        maximum = max(maximum, n1 * n2)
    return maximum
