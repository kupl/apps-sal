def pairs(arr):
    return sum((1 for i in range(len(arr) // 2) if abs(arr[i * 2] - arr[i * 2 + 1]) == 1))
