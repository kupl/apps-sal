def check(seq, elem):
    try:
        if seq.index(elem) >= 0:
            return True
    except:
        return False
