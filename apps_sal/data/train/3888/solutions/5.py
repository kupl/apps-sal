import re


def clock_degree(s):
    if not re.match(r'([0-1][0-9]|[2][0-3]):[0-5][0-9]', s):
        return "Check your time !"

    hr, sec = tuple(map(int, s.split(":")))
    hr = str((hr % 12) * 30 if hr % 12 > 0 else 360)
    sec = str(sec * 6 if sec > 0 else 360)
    return hr + ":" + sec
