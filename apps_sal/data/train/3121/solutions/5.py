def solve(arr):
    for x in arr:
        if x and -x not in arr:
            return x
