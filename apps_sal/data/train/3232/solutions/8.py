def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    return arr[arr.index(n) + 1:].index(n) + 2
