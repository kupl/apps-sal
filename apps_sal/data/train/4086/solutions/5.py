def first_non_consecutive(arr):
    for b in range(len(arr) - 1):
        if arr[b + 1] - arr[b] != 1:
            return arr[b + 1]

