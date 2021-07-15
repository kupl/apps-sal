def distinct(seq):
    newlist = []
    for eachnumber in seq:
        if eachnumber in newlist:
            continue
        else:
            newlist.append(eachnumber)
    return newlist
