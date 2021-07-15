def check(seq, elem):
    for elemseq in seq:
        if elem == elemseq:
            return True
    else:
        return False
