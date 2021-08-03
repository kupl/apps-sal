def merge_arrays(arr1, arr2):
    for i in arr2:
        arr1.append(i)
    return sorted(set(arr1))
