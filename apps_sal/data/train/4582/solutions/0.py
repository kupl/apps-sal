def group(arr):
    return [[n] * arr.count(n) for n in sorted(set(arr), key=arr.index)]
