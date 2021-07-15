def time_correct(t):
    if t == '':
        return ''
    elif t == None:
        return None
    tmp = [0, 0, 0]
    for i in t:
        if '0' <= i <= '9':
            tmp[0] += 1
        elif i == ':':
            tmp[1] += 1
        else:
            tmp[2] += 1
    if not (tmp[0] == 6 and tmp[1] == 2):
        return None
    else:
        tt = list(map(int, t.split(':')))
        tt[1]+=tt[2]//60
        tt[0]+=tt[1]//60
        tt[2]%=60
        tt[1]%=60
        tt[0] -= tt[0]//24 * 24
        return "%02d:%02d:%02d"%(tt[0],tt[1],tt[2])
