def is_sorted_and_how(arr):
    a = sorted(arr)
    if a == arr:
        return 'yes, ascending'
    elif sorted(a, reverse=True) == arr:
        return 'yes, descending'
    else:
        return 'no'
