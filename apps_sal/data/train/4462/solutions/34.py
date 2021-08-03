def adjacent_element_product(array):
    result = array[0] * array[1]
    for i in range(1, len(array) - 1):
        temp = array[i] * array[i + 1]
        if result < temp:
            result = temp
    return result
