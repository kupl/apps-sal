def array_plus_array(arr1, arr2):
    arr1sum = 0
    arr2sum = 0
    for i in arr1:
        arr1sum += i
    for i in arr2:
        arr2sum += i
    return arr1sum + arr2sum
