def adjacent_element_product(array):
    num = array[0] * array[1]
    i = 1
    while i+1 < len(array):
        if array[i]*array[i+1] > num:
            num = array[i]*array[i+1]
        i += 1
    return num
