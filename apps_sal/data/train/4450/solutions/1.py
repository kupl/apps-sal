def consecutive(arr):
    if len(arr) == 1 or len(arr) == 0:
        return 0
    (mn, mx) = (min(arr), max(arr))
    s = set(arr)
    return mx - mn - len(s) + 1
