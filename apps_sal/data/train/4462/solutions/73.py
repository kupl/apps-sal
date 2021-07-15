def adjacent_element_product(arr):
    list = []
    for number in range(len(arr)-1):
        list.append(arr[number] * arr[number+1])
    return max(list)
