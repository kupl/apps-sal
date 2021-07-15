def check(seq, elem):
    tot = 0
    for i in range(len(seq)):
        if str(seq[i]) == str(elem):
            tot += 1
    if tot > 0:
        return True
    return False
