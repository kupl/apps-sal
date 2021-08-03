def array_plus_array(arr1, arr2):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr1)):
        sum1 += arr1[i]
    for x in range(len(arr2)):
        sum2 += arr2[x]
    return sum1 + sum2
