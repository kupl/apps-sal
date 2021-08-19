def sort_two_arrays(arr1, arr2):
    ind = list(range(len(arr1)))
    a1 = [y for (x, i, y) in sorted(zip(arr2, ind, arr1))]
    a2 = [y for (x, i, y) in sorted(zip(arr1, ind, arr2))]
    return [a1, a2]
