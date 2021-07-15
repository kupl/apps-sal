def adjacent_element_product(array):
    max_prod = array[0] * array[1]
    for i in range(2, len(array)):
        temp = array[i] * array[i-1]
        if temp > max_prod:
            max_prod = temp
    return max_prod
