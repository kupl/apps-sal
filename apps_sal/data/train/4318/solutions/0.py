def hot_singles(arr1, arr2):
    a = []
    for x in arr1 + arr2:
        if x in set(arr1) ^ set(arr2) and x not in a: a.append(x)
    return a
