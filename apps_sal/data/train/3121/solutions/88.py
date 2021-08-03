def solve(arr):
    for i in arr:
        if -1 * i in arr:
            continue
        return i
