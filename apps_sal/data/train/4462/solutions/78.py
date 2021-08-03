def adjacent_element_product(array):
    index1 = 0
    index2 = 0
    max1 = -9999999
    for i in range(len(array) - 1):
        if((array[i] * array[i + 1]) > max1):
            max1 = array[i] * array[i + 1]
            index1 = i
            index2 = i + 1
    return array[index1] * array[index2]
