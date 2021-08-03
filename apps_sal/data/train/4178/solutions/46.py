def min_sum(arr):
    arr = sorted(arr)
    result = 0
    for i in range(len(arr) // 2):
        result += arr[i] * arr[0 - (i + 1)]
    return result
