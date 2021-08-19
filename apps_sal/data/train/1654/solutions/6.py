import re


def solve_runes(runes):
    m = re.match('{n}([-+*]){n}={n}$'.format(n='(0|-?[1-9?][0-9?]*)'), runes)
    if not m:
        return -1
    (l, op, r, ans) = m.groups()
    start = any((len(s) > 1 and (s[0] == '?' or s[:2] == '-?') for s in (l, r, ans)))
    check = runes.replace('=', '==')
    return next((i for i in range(start, 10) if str(i) not in runes and eval(check.replace('?', str(i)))), -1)
