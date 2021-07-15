def group(arr):
    return [[n]*arr.count(n) for i, n in enumerate(arr) if arr.index(n) == i]
