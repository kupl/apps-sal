def length_of_sequence(arr, n):
    inds = [i for (i, v) in enumerate(arr) if v == n]
    return inds[1] - inds[0] + 1 if len(inds) == 2 else 0
