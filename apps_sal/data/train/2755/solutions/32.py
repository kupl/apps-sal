def multiple_of_index(arr):
    res = []
    for i in range(1, len(arr), 1):
        if arr[i] % i == 0:
            res.append(arr[i])
    return res
