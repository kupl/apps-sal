def check(seq, elem):
    if (elem in seq or str(elem) in seq):
        return True
    else:
        return False
