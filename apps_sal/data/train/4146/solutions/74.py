def is_sorted_and_how(arr):
    return 'yes, ascending' if arr == sorted(arr) else 'yes, descending' if arr[::-1] == sorted(arr[::-1]) else 'no'
