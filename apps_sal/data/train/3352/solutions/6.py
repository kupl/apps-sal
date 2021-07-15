def find_longest(arr):
    return next(s for s in arr if len(str(s)) == len(str(max(arr))))
