def is_sorted_and_how(arr):
    a = sorted(arr)
    d = sorted(arr, reverse=True)
    if arr == a:
        return 'yes, ascending'
    elif arr == d:
        return 'yes, descending'
    else:
        return 'no'
