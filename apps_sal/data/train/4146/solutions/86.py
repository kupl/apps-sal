def is_sorted_and_how(arr):
    a = sorted(arr)
    b = sorted(arr, reverse=True)
    if arr[1] == a[1]:
        return 'yes, ascending'
    elif arr[1] == b[1]:
        return 'yes, descending'
    else:
        return 'no'
