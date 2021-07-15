def is_nice(arr):
    for x in arr:
        if x + 1 not in arr and x - 1 not in arr:
            return False
    return True and len(arr) > 0
