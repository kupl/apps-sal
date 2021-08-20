def or_arrays(arr1, arr2, p=0):
    if len(arr2) > len(arr1):
        (arr2, arr1) = (arr1, arr2)
    arr2 += [p] * (len(arr1) - len(arr2))
    return [arr1[i] | arr2[i] for i in range(len(arr1))]
