def merge_arrays(arr1, arr2):
    if arr1 == [] and arr2 == []:
        return []
    return sorted(list(set(arr1 + arr2)))
