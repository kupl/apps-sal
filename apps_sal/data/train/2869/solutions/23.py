def distinct(seq):
    out=[]
    for x in seq :
        if not x in out : out.append(x)
    return out
