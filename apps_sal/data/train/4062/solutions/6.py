def solve(arr):
    return [a for (i, a) in enumerate(arr) if all((a > b for b in arr[i + 1:]))]
