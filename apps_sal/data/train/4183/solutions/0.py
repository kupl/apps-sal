def greatest_distance(arr):
    return max((i - arr.index(x) for (i, x) in enumerate(arr)))
