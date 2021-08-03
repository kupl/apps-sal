def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    for i in range(len(arr) - 1):
        for j in range(1):
            if arr[i] > arr[i + 1]:
                continue
            else:
                return 'no'
    return 'yes, descending'
