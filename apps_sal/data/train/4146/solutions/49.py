def is_sorted_and_how(arr):
    if arr[0] < arr[1]:
        return 'yes, ascending'
    elif arr[0] > arr[1] and arr[0] > arr[2]:
        return 'yes, descending'
    else:
        return 'no'
