def is_sorted_and_how(arr):
    if arr == list(sorted(arr)) or arr == list(sorted(arr))[::-1]:
        return 'yes, ascending' if arr[0] < arr[1] else 'yes, descending'
    else:
        return 'no'
