def merge_arrays(arr1, arr2):
    arr = []
    for i in arr1:
        if i not in arr:
            arr.append(i)
    for i in arr2:
        if i not in arr:
            arr.append(i)
    return sorted(arr)
