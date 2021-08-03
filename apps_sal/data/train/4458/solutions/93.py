def time_correct(t):
    if t == '':
        return ''
    elif t == None or len(t) != 8 or len(t) == 8 and not (t[:2].isdigit() and t[2] == ':' and t[3:5].isdigit() and t[5] == ':' and t[6:].isdigit()):
        return None
    else:
        h, m, s = int(t[:2]), int(t[3:5]), int(t[6:])
        m = m + s // 60
        s = s % 60
        h = h + m // 60
        m = m % 60
        h = h % 24
        return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
