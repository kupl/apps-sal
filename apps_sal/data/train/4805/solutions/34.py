def check(seq, elem):
    try:
        seq.index(elem)
        return True
    except ValueError:
        return False
