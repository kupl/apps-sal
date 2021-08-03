import re


def time_correct(t):
    if t is None or t == '':
        return t
    if not re.match('[0-9][0-9]:[0-9][0-9]:[0-9][0-9]$', t):
        return None
    h, m, s = map(int, t.split(':'))
    if s > 59:
        s -= 60
        m += 1
    if m > 59:
        m -= 60
        h += 1
    while h > 23:
        h -= 24
    return ':'.join(f'{x:02}' for x in [h, m, s])
