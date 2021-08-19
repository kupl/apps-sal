def array_plus_array(arr1, arr2):
    total = 0
    full_list = arr1 + arr2
    for num in range(0, len(full_list)):
        total = total + full_list[num]
    return total
