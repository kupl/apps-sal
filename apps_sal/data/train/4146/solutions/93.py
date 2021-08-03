def is_sorted_and_how(arr):
    if arr[0] >= arr[1]:
        for n in range(1, len(arr)):
            if arr[n - 1] < arr[n]:
                return "no"
        return "yes, descending"
    elif arr[0] <= arr[1]:
        for n in range(1, len(arr)):
            if arr[n - 1] > arr[n]:
                return "no"
        return "yes, ascending"
    else:
        return "no"
