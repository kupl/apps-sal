def array_plus_array(arr1, arr2):
    sum1 = 0
    sum2 = 0
    for i in arr1:
        sum1 = i + sum1
    for i in arr2:
        sum2 = i + sum2
    sum = sum1 + sum2
    return sum
