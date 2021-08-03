def merge_arrays(arr1, arr2):
    merged = arr1 + arr2
    a = sorted(merged)
    res = []
    [res.append(x) for x in a if x not in res]
    return res
