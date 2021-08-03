def array_plus_array(arr1, arr2):
    counter = 0
    for i in range(len(arr1)):
        counter += arr1[i]
    for i in range(len(arr2)):
        counter += arr2[i]
    return counter
