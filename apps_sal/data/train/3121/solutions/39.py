def solve(arr):
    for a in arr:
        if -a in arr:
            continue
        if -a not in arr:
            return a
