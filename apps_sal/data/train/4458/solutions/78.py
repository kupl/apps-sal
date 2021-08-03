from re import match


def time_correct(t):
    if not t:
        return t
    g = match('^(\d{2}):(\d{2}):(\d{2})$', t)
    if g:
        h, m, s = map(int, g.groups())
        m += s // 60
        s %= 60
        h = (h + (m // 60)) % 24
        m %= 60
        return '{:02}:{:02}:{:02}'.format(h, m, s)
