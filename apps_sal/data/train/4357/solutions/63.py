def nth_smallest(arr, pos):
    for (i, x) in enumerate(sorted(arr)):
        if i == pos - 1:
            return x
