def is_sorted_and_how(arr):
    sort_arr = sorted(arr)
    sort_desc = sorted(arr, reverse=True)
    if sort_arr == arr:
        return 'yes, ascending'
    if sort_desc == arr:
        return 'yes, descending'
    else:
        return 'no'
