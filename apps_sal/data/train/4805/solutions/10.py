def check(seq, elem):
    try:
        seq.index(elem) >= 0
    except ValueError: 
        return False
    return True

