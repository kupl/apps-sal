
def capitalize(s, ind):
    ret, ixd = '', ind[::]
    ch = ixd.pop(0)
    for i, e in enumerate(s):
        if i == ch:
            ret += e.upper()
            if ixd:
                ch = ixd.pop(0)
        else:
            ret += e
    return ret
