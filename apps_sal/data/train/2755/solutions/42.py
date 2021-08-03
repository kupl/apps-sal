def multiple_of_index(arr):
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] % i == 0:
            res.append(arr[i])
    return res
