def is_sorted_and_how(arr):
    k = 0
    i = 0
    while i != len(arr) - 1:
        if arr[i] < arr[i + 1]:
            k += 1
        elif arr[i] > arr[i + 1]:
            k -= 1
        i += 1
    if k == len(arr) - 1:
        return 'yes, ascending'
    elif k == -len(arr) + 1:
        return 'yes, descending'
    else:
        return 'no'

