def array_plus_array(arr1, arr2):
    sum = 0
    sum1 = 0
    result = 0
    for i in arr1:
        sum += i
    for x in arr2:
        sum1 += x
    result += sum + sum1
    return result
