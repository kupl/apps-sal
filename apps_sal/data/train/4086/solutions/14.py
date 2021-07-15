def first_non_consecutive(arr):
    for n in range(len(arr) - 1):
        if arr[n + 1] != arr[n] + 1:
            return arr[n + 1]
    return None
