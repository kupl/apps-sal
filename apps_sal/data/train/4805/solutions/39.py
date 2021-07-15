def check(seq, elem):
    flag = False
    for i in seq:
        if str(i) == str(elem):
            flag = True
            break
    return flag
