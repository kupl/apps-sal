def binRota(arr):
    res = []
    for i in range(len(arr)):
        res.extend(arr[i][::(-1) ** i])
    return res
