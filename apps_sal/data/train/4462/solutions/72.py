def adjacent_element_product(array):
    prods = []
    for i in range(len(array)-1):
        prods.append(array[i]*array[i+1])
    return max(prods)
