import re


def time_correct(t):
    if not t:
        return t
    if not re.fullmatch('^\\d\\d:\\d\\d:\\d\\d$', t):
        return None
    (h, m, s) = map(int, t.split(':'))
    return '{:02d}'.format((h + (m + s // 60) // 60) % 24) + ':' + '{:02d}'.format((m + s // 60) % 60) + ':' + '{:02d}'.format(s % 60)
