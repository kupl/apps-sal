def adjacent_element_product(array):
    i = 1
    maximum = (array[0] * array[i])
    for c in array[:-1]:
        if (c * array[i]) > maximum:
            maximum = (c * array[i])
        i += 1
    return maximum
