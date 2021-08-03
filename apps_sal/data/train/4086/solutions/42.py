def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        next = arr[i + 1]
        if arr[i] + 1 != next:
            return next
    return None
