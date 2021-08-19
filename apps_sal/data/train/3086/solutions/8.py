def unflatten(arr):
    j = 0
    res = []
    for x in arr:
        if j > 0:
            res[-1].append(x)
            j -= 1
        elif x < 3:
            res.append(x)
        else:
            res.append([x])
            j = x - 1
    return res
