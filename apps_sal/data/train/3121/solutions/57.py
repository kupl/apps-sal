def solve(arr):
    for i in arr:
        if -1*i in arr:
            continue
        else:
            return i
