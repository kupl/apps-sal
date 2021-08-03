def time_correct(t):
    if not t:
        return t
    if len(t) != 8 or t[2] != ':' or t[5] != ":" or any(not t[i].isdigit() for i in (0, 1, 3, 4, 6, 7)):
        return None
    h, m, s = [int(t[o:o + 2]) for o in (0, 3, 6)]
    if s > 59:
        m += s // 60
        s %= 60
    if m > 59:
        h += m // 60
        m %= 60
    h %= 24
    return '{:02}:{:02}:{:02}'.format(h, m, s)
