def adjacent_element_product(array):
    biggest = -1000000
    i = 0
    while i < len(array) - 1:
        prod = array[i] * array[i + 1]
        if prod > biggest:
            biggest = prod
        i += 1
    return biggest
