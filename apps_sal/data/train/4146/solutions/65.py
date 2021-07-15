def is_sorted_and_how(arr):
    if all(arr[i] >= arr[i - 1] for i in range(1, len(arr))):
        return 'yes, ascending'
    elif all(arr[i] <= arr[i - 1] for i in range(1, len(arr))):
        return 'yes, descending'
    return 'no'
