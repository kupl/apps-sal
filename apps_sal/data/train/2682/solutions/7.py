def est_subsets(arr):
    s = set(arr)
    return 2 ** len(s) - 1
