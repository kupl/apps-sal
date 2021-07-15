def check(seq, elem):
    try:
        if seq.index(elem) >= 0:
            return True
        else:
            return False
    except:
        return False
