def penalty(nos):
    print(nos)
    pos = 0
    ret = []
    for x in range(len(nos)):
        low = 10
        tmp = ''
        for x in nos:
            if int(x[0]) <= int(low):
                if tmp != '':
                    tmp = getLowest(tmp, x)
                else:
                    tmp = x
                low = tmp[0]
        ret.append(tmp)
        # print(ret,'\t',tmp)
        nos.remove(tmp)
    return ''.join(ret)


def getLowest(s1, s2):
    res = {s1: s1, s2: s2}
    if len(s2) < len(s1):
        res[s2] = equalPad(s2, len(s1))
    elif len(s2) > len(s1):
        res[s1] = equalPad(s1, len(s2))
    # print('res',res)
    for x in range(len(res[s1])):
        if res[s1][x] < res[s2][x]:
            return s1
        elif res[s2][x] < res[s1][x]:
            return s2
    return s1


def equalPad(s0, w):
    return s0.ljust(w, s0[-1])
