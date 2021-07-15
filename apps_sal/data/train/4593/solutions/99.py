def merge_arrays(arr1, arr2):
    arr = arr1 + arr2
    arr3 = []
    for item in arr:
        if item not in arr3:
            arr3.append(item)
    return sorted(arr3)
