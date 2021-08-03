def solve(arr):
    for i in arr:
        if -1 * i not in arr:
            return i
