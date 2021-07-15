def capitalize(s,ind):
    t = [str(i) for i in s]
    a = ''
    for x in range(0, len(t)):
        if x  in ind:
            t[x] = t[x].upper()
        a += t[x]
    return a
