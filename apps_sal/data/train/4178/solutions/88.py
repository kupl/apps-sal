def min_sum(arr):
    arr = sorted(arr)
    arr_size = len(arr)
    return sum((arr[i] * arr[arr_size - i - 1] for i in range(arr_size // 2)))
