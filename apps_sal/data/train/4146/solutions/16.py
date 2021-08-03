def is_sorted_and_how(arr):
    s = sorted(arr)
    return 'yes, ascending' if arr == s else 'yes, descending' if arr == s[::-1] else 'no'
