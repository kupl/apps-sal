def sort_two_arrays(arr1, arr2):
    (indices, arrs) = (list(range(len(arr1))), (arr1, arr2))
    return [[arrs[a][i] for i in sorted(indices, key=arrs[1 - a].__getitem__)] for a in (0, 1)]
