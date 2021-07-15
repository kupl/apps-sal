def merge_arrays(arr1, arr2):
    for i in arr1:
        arr2.append(i)
    arr2.sort()
    a = list(dict.fromkeys(arr2))
    return a
