def time_correct(t):
    if not t:
        return t
    try:
        h, m, s = map(int, t.split(':'))
        m += s // 60
        s %= 60
        h += m // 60
        m %= 60
        h %= 24
        return f'{h:02}:{m:02}:{s:02}'
    except:
        return None
