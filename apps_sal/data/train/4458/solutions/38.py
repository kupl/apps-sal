def time_correct(t):
    try:
        k = t.split(':')
    except:
        return None
    if t == '':
        return ''
    if len(k) < 3:
        return None
    p = []
    res = 0
    for a in k[::-1]:
        if len(str(a)) != 2:
            return None
        if len(p) < 2:
            try:
                p.append(format((int(a) + res) % 60, '02d'))
            except:
                return None
            res = (int(a) + res - int(p[-1])) // 60
        else:
            try:
                p.append(format((int(a) + res) % 24, '02d'))
            except:
                return None
    return ':'.join(p[::-1])
