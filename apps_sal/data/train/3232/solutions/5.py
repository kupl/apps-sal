def length_of_sequence(arr, n):
    indexes = [i for i, x in enumerate(arr) if x == n]
    if len(indexes) != 2:
        return 0
    return indexes[1] - indexes[0] + 1
