import re


def time_correct(t):
    if t is None or t == "":
        return t
    elif re.match(r'\d{2}:\d{2}:\d{2}', t) is not None:
        v = (int(t[0:2]) * 3600) + (int(t[3:5]) * 60) + int(t[6:])
        if v > 86400:
            while v > 86400:
                v -= 86400
        return "{:02d}:{:02d}:{:02d}".format(int(v / 3600), int((v % 3600) / 60), (v % 36000) % 60)
    else:
        return None
