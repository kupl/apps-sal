def check(seq, elem):
    for i in range(len(seq)):
        if seq[i] == elem and type(seq[i]) == type(elem):
            return True
    return False
