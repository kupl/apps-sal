def check(seq, elem):
    valid = False
    for el in seq:
        if el == elem:
            valid = True
            break
    return valid
