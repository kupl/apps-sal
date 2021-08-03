def merge_arrays(arr1, arr2):
    l = []
    for x in arr1:
        l.append(x)
    for x in arr2:
        l.append(x)
    return sorted(list(set(l)))
