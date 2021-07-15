def est_subsets(arr):
    arr = list(set(arr))
    return 2 ** len(arr) - 1
