from itertools import accumulate

def solve(arr):
    arr = sorted(arr)
    return next((x+1 for x, i in zip(accumulate([0]+arr), arr+[0]) if i > x + 1), sum(arr)+1)
