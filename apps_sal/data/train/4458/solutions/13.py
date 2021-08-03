def time_correct(t):
    if t == '':
        return ''
    try:
        h, m, s = map(int, t.split(':'))
        m += 1 if s >= 60 else 0
        s %= 60
        h += 1 if m >= 60 else 0
        m %= 60
        h %= 24
        return f'{h:02}:{m:02}:{s:02}'
    except:
        return None
