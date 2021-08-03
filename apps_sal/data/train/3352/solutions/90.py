def find_longest(arr):
    ml = len(str(max(arr)))
    return next(x for x in arr if len(str(x)) == ml)
