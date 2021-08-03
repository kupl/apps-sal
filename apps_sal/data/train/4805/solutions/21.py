def check(seq, elem):
    for i in range(len(seq)):
        if seq[i] != elem:
            pass
        else:
            return True
        if i == len(seq) - 1:
            return False
