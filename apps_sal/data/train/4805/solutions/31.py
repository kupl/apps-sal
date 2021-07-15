def check(seq, elem):
    for i in range(len(seq)):
        if elem == seq[i]:
            return True
            break
    else:
        return False
