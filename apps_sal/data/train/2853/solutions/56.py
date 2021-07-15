def solve(arr):
    res = []
    for i, v in enumerate(arr):
        if arr[i:].count(v) == 1:
            res.append(v)

    return res
