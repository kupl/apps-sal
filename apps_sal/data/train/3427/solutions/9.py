def find_uniq(arr):
    res = sorted(arr)
    return res[0] if res[0] != res[1] else res[-1]

