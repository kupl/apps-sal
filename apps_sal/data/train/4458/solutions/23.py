from re import match


def time_correct(t):
    if not t:
        return t
    elif not match('\\d\\d\\:\\d\\d\\:\\d\\d', t):
        return None
    fragments = list(map(int, t.split(':')))
    if fragments[2] >= 60:
        fragments[1] += 1
        fragments[2] -= 60
    if fragments[1] >= 60:
        fragments[0] += 1
        fragments[1] -= 60
    fragments[0] %= 24
    return '{:02}:{:02}:{:02}'.format(*fragments)
