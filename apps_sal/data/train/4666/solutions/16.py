def array_plus_array(arr1, arr2):
    arr1.extend(arr2)
    sum = 0
    for i in arr1:
        sum = sum + i
    return sum
