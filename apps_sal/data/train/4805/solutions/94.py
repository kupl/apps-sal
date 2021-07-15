def check(seq, elem):
    seq.append(elem)
    return bool(seq.count(elem) - 1)

