def capitalize(s):
    al = list(s)
    ab = list(s)
    l = []
    for i in range(0,len(al)):
        if i % 2 == 0:
            al[i] = al[i].upper()
        else:
            ab[i] = al[i].upper()
    l.append(''.join(al))
    l.append(''.join(ab))
    return l
