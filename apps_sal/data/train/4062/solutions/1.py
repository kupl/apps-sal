def solve(arr):
    return [a for (i, a) in enumerate(arr) if all((x < a for x in arr[i + 1:]))]
