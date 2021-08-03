def adjacent_element_product(array):
    maximum = array[0] * array[1]
    for number in range(1, len(array) - 1):
        if array[number] * array[number + 1] > maximum:
            maximum = int(array[number]) * int(array[number + 1])
    return maximum
