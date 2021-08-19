def find_in_array(seq, fn):
    return next((i for (i, j) in enumerate(seq) if fn(j, i)), -1)
