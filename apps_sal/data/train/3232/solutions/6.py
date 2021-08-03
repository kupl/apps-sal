def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    else:
        return arr.index(n, arr.index(n) + 1) - arr.index(n) + 1
