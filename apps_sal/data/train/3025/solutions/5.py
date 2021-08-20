def locate(seq, value):
    clean = []
    return value in unfold(clean, seq)


def unfold(clean, seq):
    """transform seq into 1d array"""
    for s in seq:
        if type(s) == str:
            clean.append(s)
        else:
            clean = list(set(unfold(clean, s)))
    return clean
