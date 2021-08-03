def is_sorted_and_how(arr):
    x = sorted(arr)
    if x == arr:
        return 'yes, ascending'
    elif x[::-1] == arr:
        return 'yes, descending'
    else:
        return 'no'
