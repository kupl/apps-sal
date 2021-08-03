def solve(arr):
    res = []

    for i in range(len(arr)):
        if arr[i] not in arr[i + 1:]:
            res.append(arr[i])

    return res
