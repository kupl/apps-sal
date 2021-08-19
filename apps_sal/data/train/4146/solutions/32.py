def is_sorted_and_how(arr):
    for index in range(len(arr))[2:]:
        if (arr[index] <= arr[index - 1]) != (arr[index - 1] <= arr[index - 2]):
            return 'no'
    return 'yes, descending' if arr[1] <= arr[0] else 'yes, ascending'
