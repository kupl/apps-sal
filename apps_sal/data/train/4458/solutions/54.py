import re


def time_correct(t):
    if not isinstance(t, str):
        return None
    if t == '':
        return t
    if not re.match(r'^\d{2}:\d{2}:\d{2}$', t):
        return None

    t_tot = sum(60**i * int(e) for i, e in enumerate(t.split(':')[::-1]))
    return f'{t_tot // 3600 % 24:02}:{t_tot // 60 % 60:02}:{t_tot % 60:02}'
