def solve(arr):
    for x in arr:
        if (-x) not in arr and x in arr or x not in arr and (-x) in arr:
            return x
