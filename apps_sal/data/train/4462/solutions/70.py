def adjacent_element_product(array):
    res = []
    start = array[0]

    for num in array[1:]:
        res.append(start * num)
        start = num
    
    return max(res)
