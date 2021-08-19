def first_n_smallest(lst, n):
    std = sorted(enumerate(lst), key=lambda e: e[1])[:n]
    return [n for (i, n) in sorted(std)]
