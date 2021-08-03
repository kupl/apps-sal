def time_correct(t):
    if t == '':
        return ''
    if t is None:
        return None
    if not __import__('re').match(r'^\d\d:\d\d:\d\d', t):
        return None
    h, m, s = [int(x) for x in t.split(':')]
    while s >= 60:
        s -= 60
        m += 1
    while m >= 60:
        m -= 60
        h += 1
    while h >= 24:
        h -= 24
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
