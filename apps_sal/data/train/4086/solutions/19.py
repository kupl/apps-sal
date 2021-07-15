def first_non_consecutive(arr):
    for ind in range(1, len(arr)):
        if arr[ind] - arr[ind-1] > 1:
            return arr[ind]
