def adjacent_element_product(array):
    length = len(array)
    res = []
    for i in range(length):
        if i < length-1:
            res.append(array[i] * array[i+1])
            
    res.sort()
    return res[-1]
