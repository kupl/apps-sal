def check(seq, elem):
    if str(elem) not in str(seq):
        return False
    elif elem not in seq:
        return False
    else:
        return True

