def min_sum(arr):
    arr = sorted(arr)
    n = 0
    while len(arr) > 0:
        n += arr.pop(0) * arr.pop()

    return n
