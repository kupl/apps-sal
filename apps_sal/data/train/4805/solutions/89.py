def check(seq, elem):
    print(seq, elem)
    for i in seq:
        if i == elem:
            return True
    return False
