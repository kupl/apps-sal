def array_plus_array(arr1, arr2):
    sum_list = []
    for (i1, i2) in zip(arr1, arr2):
        sum_list.append(i1 + i2)

    return sum(sum_list)
