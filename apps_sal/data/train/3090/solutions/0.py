def find_2nd_largest(arr):
    arr = sorted((i for i in set(arr) if type(i) == int))
    return arr[-2] if len(arr) > 1 else None
