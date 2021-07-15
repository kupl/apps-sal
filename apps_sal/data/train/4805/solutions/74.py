def check(seq, elem):
    count = 0
    for item in seq:
        if item == elem:
            count += 1
        else:
            count += 0
    if count > 0:
        return True
    else:
        return False
