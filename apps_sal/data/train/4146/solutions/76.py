def is_sorted_and_how(arr):
    sort_arr = sorted(arr)
    des_arr = sorted(arr)[::-1]
    if arr == sort_arr:
        return 'yes, ascending'
    if arr == des_arr:
        return 'yes, descending'
    return 'no'
