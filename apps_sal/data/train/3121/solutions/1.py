def solve(arr):
    for a in arr:
        if -a not in arr:
            return a
