def check(seq, elem):
    for i in range(len(seq)):
        if seq[i] == elem:
            return True
    else:
        return False


check([1, 2, 3, 's', 5], 'w')
