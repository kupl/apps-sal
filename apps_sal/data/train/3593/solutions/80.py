def capitalize(s, ind):
    sl = len(s)
    ls = []
    st = ''
    for i in s:
        ls.append(i)
    for i in range(sl):
        if i in ind:
            ls[i] = ls[i].upper()
    for i in ls:
        st += i
    return st
