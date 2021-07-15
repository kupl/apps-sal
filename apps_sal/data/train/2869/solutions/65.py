def distinct(seq):
    clean = []
    for i in seq:
        if i not in clean:
            clean.append(i)
    return clean
