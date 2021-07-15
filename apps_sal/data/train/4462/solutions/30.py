def adjacent_element_product(array):
    max = array[0] * array[1]
    for i in range(len(array) - 1):
        temp = array[i] * array[i + 1]
        if(max < temp):
            max = temp
    return max
