def locate(seq, value): 
    f = 0
    for e in seq:
        if type(e) == list and not f:
            f = locate(e, value)
        elif e == value:
            f = 1
    return f

