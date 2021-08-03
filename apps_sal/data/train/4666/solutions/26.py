def array_plus_array(arr1, arr2):
    sum = 0
    for i in range(max(len(arr1), len(arr2))):
        sum = sum + arr1[i] + arr2[i]
    return sum
