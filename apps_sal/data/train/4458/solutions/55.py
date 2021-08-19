from datetime import datetime


def time_correct(t):
    if t == '':
        return ''
    if not t:
        return None
    t = t.split(':')
    if len(t) < 3:
        return None
    try:
        t = list(map(int, t))
    except:
        return None
    seco = t[2] % 60
    minu = t[1] % 60 + t[2] // 60
    hour = t[0] % 24 + t[1] // 60
    hour = str(hour % 24 + minu // 60).zfill(2)
    minu = str(minu % 60 + seco // 60).zfill(2)
    seco = str(seco % 60).zfill(2)
    return ':'.join([hour, minu, seco])
