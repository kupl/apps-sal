def minimum_steps(arr, n):
    arr = sorted(arr)
    s = 0
    for i, v in enumerate(arr):
        s += v
        if s >= n:
            return i
