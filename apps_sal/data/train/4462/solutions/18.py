def adjacent_element_product(array):
    return(max([j*array[i+1] for i,j in enumerate(array[:-1])]))
