def is_sorted_and_how(arr):
    a = sorted(arr)
    d = sorted(arr, reverse=True)
    return 'yes, ascending' if arr == a else 'yes, descending' if arr == d else 'no'
