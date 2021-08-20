def time_correct(t):
    if t is None:
        return None
    if t is '':
        return ''
    try:
        (h, m, s) = map(int, t.split(':'))
        m += s // 60
        s = s % 60
        h += m // 60
        m = m % 60
        h = h % 24
        return '{:02}:{:02}:{:02}'.format(h, m, s)
    except:
        return None
