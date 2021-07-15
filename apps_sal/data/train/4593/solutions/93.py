def merge_arrays(arr1, arr2):
    arr3 = []
    for i in set(arr1):
        arr3.append(i)
    for j in set(arr2):
        if j not in arr1:
            arr3.append(j)
    return sorted(arr3)
