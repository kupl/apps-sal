import re


def time_correct(t):
    if t == '':
        return ""
    if not t:
        return
    if not re.match(r'\d{2}:\d{2}:\d{2}', t):
        return None
    s = int(t[6:])
    m = int(t[3:5])
    h = int(t[:2])
    if s >= 60:
        m += s // 60
        s = s % 60
    if m >= 60:
        h += m // 60
        m = m % 60
    if h >= 24:
        h = h % 24
    return ':'.join(str(i).zfill(2) for i in [h, m, s])
