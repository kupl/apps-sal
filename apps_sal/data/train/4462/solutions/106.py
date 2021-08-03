def adjacent_element_product(array):
    i = 0
    c = array[0] * array[1]
    while i < len(array) - 1:
        if array[i] * array[i + 1] > c:
            c = array[i] * array[i + 1]
        i += 1
    return c
