def adjacent_element_product(array):
    return max(m*n for m, n in zip(array, array[1:]))
   

