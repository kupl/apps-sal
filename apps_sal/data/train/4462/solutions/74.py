def adjacent_element_product(array):
    max_prod = array[0] * array[1]

    if len(array) > 2:
        for i in range(1, len(array) - 1):
            if array[i] * array[i + 1] > max_prod:
                max_prod = array[i] * array[i + 1]

    return max_prod
