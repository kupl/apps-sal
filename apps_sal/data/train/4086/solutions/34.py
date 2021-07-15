def first_non_consecutive(arr):
    for ix in range(len(arr) - 1):
        if arr[ix] + 1 != arr[ix + 1]:
            return arr[ix + 1]
