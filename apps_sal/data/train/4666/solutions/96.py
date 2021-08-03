def array_plus_array(arr1, arr2):
    i = 0
    l = 0
    o = 0

    while i < len(arr1):
        l = l + arr1[i]
        i += 1

    i = 0

    while i < len(arr2):
        o = o + arr2[i]
        i += 1

    l = l + o
    return l
