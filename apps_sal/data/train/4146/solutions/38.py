def is_sorted_and_how(arr):
    asc = sorted(arr)
    des = sorted(arr, reverse=True)
    if arr == asc:
        return 'yes, ascending'
    elif arr == des:
        return 'yes, descending'
    elif arr != (asc or des):
        return 'no'
