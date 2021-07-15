def is_sorted_and_how(arr):
    sorted_arr = sorted(arr)
    if sorted_arr == arr:
        return 'yes, ascending'
    elif sorted_arr[::-1] == arr:
        return 'yes, descending'
    return 'no'
