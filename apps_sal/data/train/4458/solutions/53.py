import re


def valid_format(s):
    return bool(re.match('^\\d\\d:\\d\\d:\\d\\d$', s))


def time_correct(t):
    if not t:
        return t
    if not valid_format(t):
        return None
    (h, m, s) = map(int, t.split(':'))
    total = 3600 * h + 60 * m + s
    s = total % 60
    m = total // 60 % 60
    h = (total - m * 60 - s) // 3600 % 24
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
