def time_correct(t):
    if t is None:
        return
    if t == "":
        return ""
    if len(t) != 8:
        return
    try:
        h, m, s = [int(i) for i in t.split(':')]
    except:
        return
    if s >= 60:
        s = s - 60
        m = m + 1
    if m >= 60:
        m = m - 60
        h = h + 1
    h = h % 24
    return ':'.join([str(h).rjust(2, '0'), str(m).rjust(2, '0'), str(s).rjust(2, '0')])
