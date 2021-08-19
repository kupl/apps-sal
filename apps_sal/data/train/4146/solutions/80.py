def is_sorted_and_how(arr):
    sort = 'yes, ascending'
    sort2 = 'yes, descending'
    if arr[0] > arr[len(arr) - 1]:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                sort = 'no'
    if arr[0] < arr[len(arr) - 1]:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sort = 'no'
    if sort != 'no':
        if arr[0] > arr[len(arr) - 1]:
            return sort2
        elif arr[0] < arr[len(arr) - 1]:
            return sort
    else:
        return sort
