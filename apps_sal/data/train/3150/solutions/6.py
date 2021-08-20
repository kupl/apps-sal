def binary_cleaner(seq):
    (list_a, list_b) = ([], [])
    for (k, v) in enumerate(seq):
        if v > 1:
            list_b.append(k)
        else:
            list_a.append(v)
    return (list_a, list_b)
