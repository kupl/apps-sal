def time_correct(t):
    if t is None:
        return None
    if t == '':
        return ''
    if t.count(':') != 2 or len(t) != 8:
        return None
    tt = t.replace(':', '')
    if not tt.isdigit():
        return None
    (h, m, s) = (int(tt[0:2]), int(tt[2:4]), int(tt[4:]))
    if s >= 60:
        m += 1
        s %= 60
    if m >= 60:
        h += 1
        m %= 60
    h %= 24
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
