from functools import reduce

def solve(arr):
    return reduce(int.__mul__, map(len, map(set, arr)))
