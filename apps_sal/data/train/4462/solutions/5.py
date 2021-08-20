def adjacent_element_product(array):
    new_list = []
    sum = 1
    for e in range(len(array)):
        if e == 0:
            sum *= array[e] * array[e + 1]
            new_list.append(sum)
            sum = 1
        elif e in range(1, len(array) - 1):
            sum *= array[e - 1] * array[e]
            new_list.append(sum)
            sum = 1
            sum *= array[e + 1] * array[e]
            new_list.append(sum)
            sum = 1
        else:
            sum *= array[e] * array[e - 1]
    return max(new_list)
