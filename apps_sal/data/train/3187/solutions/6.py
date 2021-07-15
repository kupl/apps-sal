def sum_nested(lst):
    s = 0
    for l in lst:
        if type(l) == list:
            s += sum_nested(l)
        else:
            s += l
    return s
