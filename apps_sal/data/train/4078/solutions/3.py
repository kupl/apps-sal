def first_n_smallest(arr, n):
    return [x[1] for x in sorted(sorted(enumerate(arr), key=lambda x: x[1])[:n])]
