def multiple_of_index(arr):
    res = []
    for (c, a) in enumerate(arr):
        if c != 0 and a % c == 0:
            res.append(a)
    return res
