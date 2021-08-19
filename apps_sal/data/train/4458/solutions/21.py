import re


def time_correct(t):
    if not t:
        return t
    if not re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}$', str(t)):
        return None
    tl = list(map(int, t.split(':')))
    for i in range(2, 0, -1):
        while tl[i] >= 60:
            tl[i] -= 60
            tl[i - 1] += 1
    while tl[0] >= 24:
        tl[0] -= 24
    return ':'.join(['{:02d}'.format(te) for te in tl])
