def min_sum(arr):
    arr = sorted(arr)
    return sum(arr.pop(0) * arr.pop(-1) for i in range(len(arr) // 2))
