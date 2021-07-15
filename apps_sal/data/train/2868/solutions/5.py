def is_nice(arr):
    if len(arr) == 0:
        return False
    for n in arr:
        if n-1 not in arr and n+1 not in arr:
            return False
    return True
