def adjacent_element_product(array):
    m = 0
    max = array[0]*array[1]
    for i in range(1, len(array)-1) :
        m = array[i]*array[i+1]
        if m > max : max = m
    return max # max product
