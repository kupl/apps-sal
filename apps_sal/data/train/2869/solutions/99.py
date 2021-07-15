def distinct(seq):
    c=[]
    for i in seq:
        if i not in c:
            c.append(i)
    return c
