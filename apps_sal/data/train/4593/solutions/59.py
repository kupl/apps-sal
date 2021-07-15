def merge_arrays(arr1, arr2):
    merge=list(set(arr1).union(set(arr2)))
    merge.sort()
    return merge
