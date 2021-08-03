def solve(s):
    slist = []
    for i in s:
        slist.append(i)
    c = 0
    res = []
    for i in slist:
        if slist[c] == ' ':
            res.append(c)
            slist.remove(slist[c])
        c += 1
    s_rev = slist[::-1]
    c = 0
    for i in s_rev:
        if c + 1 in res:
            s_rev[c] = s_rev[c] + " "
        c += 1
    return ''.join(i for i in s_rev)
