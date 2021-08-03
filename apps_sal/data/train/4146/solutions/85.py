def is_sorted_and_how(arr):
    a = arr
    if a == sorted(arr):
        return 'yes, ascending'
    elif a == sorted(arr, reverse=True):
        return 'yes, descending'
    else:
        return 'no'
