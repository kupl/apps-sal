def solve(arr):
    n = len(arr)
    res = []
    for i in range(n - 1, -1, -1):
        if arr[i] not in res:
            res.append(arr[i])
    res.reverse()
    return res
