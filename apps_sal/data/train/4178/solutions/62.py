def min_sum(arr):
    arr = sorted(arr)
    return sum(pair[0] * pair[1] for pair in zip(arr[:len(arr) // 2], arr[len(arr) // 2:][::-1]))
