def solve(arr):
    return [n for i, n in enumerate(arr) if n > max(arr[i + 1:], default=0)]
