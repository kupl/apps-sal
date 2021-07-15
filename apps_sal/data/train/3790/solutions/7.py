def solve(arr):
    from functools import reduce
    return reduce(lambda a,b: a*b, [len(set(a)) for a in arr])
