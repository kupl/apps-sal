def odd_one(arr):
    arr = list(map(lambda x: x % 2 == 0, arr))
    if arr.count(True) == 1:
        return arr.index(True)
    elif arr.count(False) == 1:
        return arr.index(False)
    else:
        return -1
