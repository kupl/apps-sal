def dominator(arr):
    for el in arr:
        if arr.count(el) > len(arr) / 2:
            return el
    return -1
