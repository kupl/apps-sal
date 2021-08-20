def solve(arr):
    for x in arr:
        if not x * -1 in arr:
            return x
