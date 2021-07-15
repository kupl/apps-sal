def is_sorted_and_how(arr):
    if sorted(arr) == arr:
        return 'yes, ascending'
    elif sorted(arr[::-1]) == arr[::-1]:
        return 'yes, descending'
    else:
        return 'no'
