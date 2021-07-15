def adjacent_element_product(array):
    new_list =[]
    for i in range (len(array)):
        if array[i] != array[-1]:
            new_list.append(array[i] * array[i+1])
    new_list.sort()
    return new_list[-1]
