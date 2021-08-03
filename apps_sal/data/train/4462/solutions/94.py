def adjacent_element_product(array):
    biggest = array[0] * array[1]
    index = 1
    while index < len(array):
        if array[index] * array[index - 1] > biggest:
            biggest = array[index] * array[index - 1]
        index += 1
    return biggest
