def multiple_of_index(arr):
    res = []
    if arr[0] == 0:
        res.append(0)
    for i in range(1, len(arr)):
        try:
            if arr[i] % i == 0:
                res.append(arr[i])
        except:
            res.append(0)
    return res
