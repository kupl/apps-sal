def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    left = arr.index(n)
    right = arr.index(n, left + 1)
    return right - left + 1
