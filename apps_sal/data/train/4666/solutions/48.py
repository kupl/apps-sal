def array_plus_array(arr1,arr2):
    result1 = 0
    result2 = 0
    result = 0
    for number in arr1:
        result1 += number
    for number in arr2:
        result2 += number
    result = result1 + result2
    return result
    pass
