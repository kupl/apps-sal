def is_sorted_and_how(arr):
    x = list(arr)
    x.sort()
    if arr == x:
        return 'yes, ascending'
    elif arr[::-1] == x:
        return 'yes, descending'
    else:
        return 'no'
