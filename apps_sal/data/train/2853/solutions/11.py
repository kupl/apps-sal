def solve(arr): return [e for i, e in enumerate(arr) if e not in arr[i + 1:]]
