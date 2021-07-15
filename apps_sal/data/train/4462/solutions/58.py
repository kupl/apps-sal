def adjacent_element_product(array):
    max = - float('inf')
    for i in range(1,len(array)):
            if array[i] * array[i-1] > max:
                max = array[i] * array[i-1]
    return max
