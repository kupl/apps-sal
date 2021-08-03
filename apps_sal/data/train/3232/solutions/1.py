def length_of_sequence(arr, n):
    return (len(arr) - arr[::-1].index(n) - 1) - arr.index(n) + 1 if arr.count(n) == 2 else 0
