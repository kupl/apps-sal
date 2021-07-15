def solve(arr):
    for val in arr:
        if -1*val not in arr:
            return val

