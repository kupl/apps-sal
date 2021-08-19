def array_plus_array(arr1, arr2):
    d = 0
    for (a1, a2) in zip(arr1, arr2):
        x = a1 + a2
        d += x
    return d
