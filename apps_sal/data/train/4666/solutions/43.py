def array_plus_array(arr1,arr2):
    arr1_sum = 0
    arr2_sum = 0
    for i in arr1:
        arr1_sum = arr1_sum + i
    for j in arr2:
        arr2_sum = arr2_sum + j
    total_sum = arr1_sum + arr2_sum
    return total_sum
        

