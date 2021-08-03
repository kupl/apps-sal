def est_subsets(arr):
    return 2**len(dict.fromkeys(arr)) - 1
