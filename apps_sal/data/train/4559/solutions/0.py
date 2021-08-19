def ones_complement(n):
    return n.translate(str.maketrans('01', '10'))
