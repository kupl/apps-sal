def distinct(seq):
    unique = []
    for x in seq:
        if x not in unique:
            unique.append(x)
    return unique
