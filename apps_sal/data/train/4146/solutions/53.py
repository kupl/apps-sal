def is_descending(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            return False
    return True


def is_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True


def is_sorted_and_how(arr):
    if is_ascending(arr) == True:
        return 'yes, ascending'
    if is_descending(arr) == True:
        return 'yes, descending'
    else:
        return 'no'
