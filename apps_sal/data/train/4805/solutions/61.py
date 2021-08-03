def check(seq, elem):
    for i in range(0, len(seq)):
        if seq[i] == elem:
            return True
        i += 1
    else:
        return False
