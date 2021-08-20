def min_sum(arr):
    arr = sorted(arr)
    mid = len(arr) // 2
    return sum((a * b for (a, b) in zip(arr[:mid], reversed(arr[mid:]))))
