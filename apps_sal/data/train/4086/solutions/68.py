def first_non_consecutive(arr):
    for int in range(1, len(arr)):
        if arr[int] - arr[int - 1] != 1:
            return arr[int]
    return None
