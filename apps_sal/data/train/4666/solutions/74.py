def array_plus_array(arr1, arr2):
    x = 0
    for i in range(len(arr1)):
        x = arr1[i] + x
    for j in range(len(arr2)):
        x = arr2[j] + x
    return x
