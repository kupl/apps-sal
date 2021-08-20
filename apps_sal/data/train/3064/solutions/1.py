def transpose(arr):
    if arr and (not any(map(bool, arr))):
        return [[]]
    return list(map(list, zip(*arr)))
