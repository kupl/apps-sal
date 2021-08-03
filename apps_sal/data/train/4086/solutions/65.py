def first_non_consecutive(arr):
    n = 0
    while n < len(arr) - 1:
        if arr[n + 1] - arr[n] != 1:
            return arr[n + 1]
        n += 1
