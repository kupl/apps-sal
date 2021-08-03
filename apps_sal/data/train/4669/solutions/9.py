def beggars(values, n):
    retList = [0] * n
    if not n:
        return []
    for idx, i in enumerate(values):
        retList[idx % n] += i
    return retList
