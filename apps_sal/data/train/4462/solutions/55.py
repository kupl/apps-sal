def adjacent_element_product(array):
    new_list = []
    for x in range(len(array)):
        if x+1 >= len(array):
            break
        else:
            new_list.append(array[x] * array[x+1])
    return max(new_list)
