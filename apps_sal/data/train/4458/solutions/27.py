import re


def time_correct(t):
    if t == None:
        return None
    pattern = '[0-9][0-9]:[0-9][0-9]:[0-9][0-9]'
    if re.search(pattern, t):
        t = t.split(':')[::-1]
        for i in range(0, 2):
            if int(t[i]) > 59:
                t[i + 1] = str(int(t[i + 1]) + int(t[i]) // 60)
                t[i] = str(int(t[i]) % 60)
        t[2] = str(int(t[2]) % 24)
        return ':'.join((i.zfill(2) for i in t[::-1]))
    elif len(t) > 0:
        return None
    else:
        return t
