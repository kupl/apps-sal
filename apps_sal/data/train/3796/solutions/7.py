def or_arrays(arr1, arr2, o=0):
    xs = []
    i = 0
    while i < len(arr1) and i < len(arr2):
        xs.append(arr1[i] | arr2[i])
        i += 1
    while i < len(arr1):
        xs.append(arr1[i] | o)
        i += 1
    while i < len(arr2):
        xs.append(arr2[i] | o)
        i += 1
    return xs
