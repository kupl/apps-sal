def solve(arr):
    return [a for i, a in enumerate(arr) if a not in arr[i + 1:]]
