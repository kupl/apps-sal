def pair_zeros(arr, *other):

    return [n for i, n in enumerate(arr) if n != 0 or arr[:i + 1].count(0) % 2 == 1]
