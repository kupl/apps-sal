def binRota(arr):
    res = []

    for i in range(len(arr)):
        if i % 2 == 1:
            res.extend(arr[i][::-1])
        else:
            res.extend(arr[i])

    return res
