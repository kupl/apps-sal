import re


def time_correct(t):
    if t in [None, '']:
        return t
    if not re.match('\\d\\d\\:\\d\\d\\:\\d\\d', t):
        return None
    parts = list(map(int, t.split(':')))
    for i in range(2, 0, -1):
        parts[i - 1] += parts[i] // 60
        parts[i] %= 60
    parts[0] %= 24
    return ':'.join(('{:02}'.format(p) for p in parts))
