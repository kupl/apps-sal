def check(seq, elem):
    for i in seq:
        if elem == i:
            return True
    for i in seq:
        if elem != i:
            return False
