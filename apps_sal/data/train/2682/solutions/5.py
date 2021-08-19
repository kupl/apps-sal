def est_subsets(arr):
    # we first count the number of unique elements m
    # then we use the mathematical property that there is 2**m - 1 non-empty
    # sets that can be created by combination of m elements
    m = len(set(arr))
    return 2**m - 1
