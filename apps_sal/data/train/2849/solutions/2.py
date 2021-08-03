def peak(arr):
    sl, sr = 0, sum(arr)
    for i, v in enumerate(arr):
        sr -= v
        if sr == sl:
            return i
        elif sl > sr:
            return -1
        sl += v
