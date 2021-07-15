def find_2nd_largest(arr):
    return next(iter(sorted(n for n in set(arr) if type(n) == int)[-2:-1]), None)
