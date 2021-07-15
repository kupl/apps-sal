def dominator(arr):
    half_length = len(arr) / 2
    for e in arr:
        if arr.count(e) > half_length:
            return e
    return -1

