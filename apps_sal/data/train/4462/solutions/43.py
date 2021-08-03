def adjacent_element_product(array):
    l = array[-2] * array[-1]
    for i in range(len(array) - 2):
        l = max(l, array[i] * array[i + 1])
    return l
