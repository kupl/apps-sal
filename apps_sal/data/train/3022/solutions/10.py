def two_highest(arg1):
    l=[]
    for x in arg1:
        if type(x)!=int:
            return False
        else:
            l.append(x)
    a=set(l)
    return sorted(a,reverse=True)[:2]
