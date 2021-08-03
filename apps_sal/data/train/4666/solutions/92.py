def array_plus_array(arr1, arr2):
    total = 0
    arr1.extend(arr2)
    for num in arr1:
        total += num
    return total
