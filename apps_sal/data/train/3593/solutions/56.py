def capitalize(s, ind):
    s = list(s)
    for i in range(len(ind)):
        if ind[i] > len(s):
            s = s
        else:
            s[ind[i]] = s[ind[i]].upper()
    return ''.join(s)
