def distinct(seq):
    v=[]
    for a in seq:
        if a not in v:
            v.append(a)
    return v
