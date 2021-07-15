def merge_arrays(arr1, arr2):
    unique = set(arr1)
    unique.update(arr2)
    return sorted(list(unique))
