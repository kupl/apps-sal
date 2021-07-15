def capitalize(s):
    st = list(s)
    caps = []
    for i in range(1,len(st),2):
        st[i] = st[i].upper()
    caps.append(''.join(st))
    st = list(s)
    for i in range(0,len(st),2):
        st[i] = st[i].upper()
    caps.append(''.join(st))
    return caps[::-1]
