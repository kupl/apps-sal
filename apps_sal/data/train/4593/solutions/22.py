def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1 + arr2))) if arr1 or arr2 else []
