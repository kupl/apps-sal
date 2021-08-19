def solve(arr):
    return [v for (i, v) in enumerate(arr) if v not in arr[i + 1:]]
