def invert(lst):
    if len(lst) > 0:
        newlst = [i * -1 for i in lst]
        return newlst
    else:
        return lst
    pass
