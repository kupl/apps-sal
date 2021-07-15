def two_highest(arg1):
    arg1 = sorted(arg1, reverse=True)
    res = []
    for i in range(len(arg1)):
        if len(res) == 2:
            break
        if arg1[i] not in res:
            res.append(arg1[i])
    return res
