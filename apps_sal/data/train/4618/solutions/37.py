def positive_sum(arr):
    res = []
    for x in arr:
        if x > 0:
            res.append(x)
    return sum(res)
