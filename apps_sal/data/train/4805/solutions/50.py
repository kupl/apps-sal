def check(seq, elem):
    for i in range(len(seq)):
        if elem in seq:
            return True
    return False
