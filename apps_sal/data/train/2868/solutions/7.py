def is_nice(arr):
    if not arr:
        return False

    for x in arr:
        if x - 1 not in arr and x + 1 not in arr:
            return False
    return True
