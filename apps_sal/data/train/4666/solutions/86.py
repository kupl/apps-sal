def array_plus_array(arr1, arr2):
    if not arr1:
        return None
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] + arr2[i]
    return sum
