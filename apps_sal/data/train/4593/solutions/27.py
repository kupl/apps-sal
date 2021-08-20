def merge_arrays(arr1, arr2):
    arr = []
    for el in arr2:
        if el not in arr:
            arr.append(el)
    for el in arr1:
        if el not in arr:
            arr.append(el)
    return sorted(arr)
