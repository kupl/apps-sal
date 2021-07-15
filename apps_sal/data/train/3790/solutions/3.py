from functools import reduce


def solve(arr):
    return reduce(int.__mul__, (len(set(lst)) for lst in arr))
