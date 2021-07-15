def solve(arr):
    arr = set(arr)
    for item in arr:
        if not (sum(arr) - item):
            return item
