def adjacent_element_product(array):
    max = array[0] * array[1]
    for i in range(2, len(array)):
        if array[i] * array[i - 1] > max:
            max = array[i] * array[i - 1]
    return max
