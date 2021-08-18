def is_sorted_and_how(arr):
    if arr[0] == sorted(arr)[0]:
        return 'yes, ascending'
    elif arr[0] == sorted(arr)[-1]:
        return 'yes, descending'
    else:
        return 'no'
