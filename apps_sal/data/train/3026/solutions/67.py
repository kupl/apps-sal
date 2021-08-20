def min_value(digits):
    lostlist = ''
    for i in sorted(list(set(digits))):
        lostlist += str(i)
    return int(lostlist)
