def first_n_smallest(arr, n):
    for i in range(len(arr) - n):
        arr.pop(len(arr) - 1 - arr[::-1].index(max(arr)))
    return arr
