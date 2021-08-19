def distinct(seq):
    unique = []
    for c in seq:
        if c not in unique:
            unique.append(c)
    return unique
