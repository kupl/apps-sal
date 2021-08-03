def check(seq, elem):
    return (False, True)[seq.count(elem) > 0]
