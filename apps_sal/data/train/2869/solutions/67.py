def distinct(seq):
    l=set(seq)
    g=[]
    for i in seq:
        if i in l:
            g.append(i)
            l.remove(i)
    return g
