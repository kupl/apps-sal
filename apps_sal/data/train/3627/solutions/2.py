def sort_two_arrays(arr1, arr2):
    indices, arrs = list(range(len(arr1))), (arr1, arr2)
    return [[arrs[a][i] for i in sorted(indices, key=arrs[1-a].__getitem__)] for a in (0, 1)]


# one-liner
#sort_two_arrays = lambda a1, a2: [[(a1, a2)[a][i] for i in sorted(range(len(a1)), key=(a1, a2)[1-a].__getitem__)] for a in (0, 1)]

