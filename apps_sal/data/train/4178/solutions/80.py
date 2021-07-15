def min_sum(arr):
    result = 0
    arr = sorted(arr)
    for i in range(len(arr) // 2):
        result += arr[i] * arr[-i - 1]
    return result
