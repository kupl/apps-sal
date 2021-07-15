def adjacent_element_product(array):
    arr_max=[]
    for i in range(len(array)-1):
        arr_max.append(array[i]*array[i+1])
    return max(arr_max)
