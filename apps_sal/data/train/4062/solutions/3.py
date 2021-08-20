def solve(arr):
    return [n for (i, n) in enumerate(arr) if all((n > x for x in arr[i + 1:]))]
