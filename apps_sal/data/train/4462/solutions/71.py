def adjacent_element_product(array):
    return max([array[e]*array[e+1] for e in range(len(array)-1)])
