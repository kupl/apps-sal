def get_min_max(seq):
    max = seq[0]
    min = seq[0]
    for a in seq:
        if a > max:
            max = a
        if a < min:
            min = a
    return (min, max)
