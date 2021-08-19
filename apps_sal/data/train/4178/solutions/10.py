def min_sum(arr):
    arr = sorted(arr)
    l = len(arr) // 2
    return sum((a * b for (a, b) in zip(arr[:l], arr[l:][::-1])))
