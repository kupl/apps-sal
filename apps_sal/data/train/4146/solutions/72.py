def is_sorted_and_how(arr):
    arr_asc = sorted(arr)
    return 'yes, ascending' if arr == arr_asc else 'yes, descending' if arr == arr_asc[::-1] else 'no'
