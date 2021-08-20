def multiple_of_index(arr):
    print(arr)
    res = []
    for x in range(len(arr)):
        if x != 0 and arr[x] % x == 0:
            res.append(arr[x])
    return res
