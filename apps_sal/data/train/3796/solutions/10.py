def or_arrays(arr1, arr2, default = 0):
    if len(arr1) < len(arr2):
        arr1 += [default]* (len(arr2) - len(arr1))
    if len(arr2) < len(arr1):
        arr2 += [default]* (len(arr1) - len(arr2))
    return [x|y for x,y in zip(arr1,arr2)]
