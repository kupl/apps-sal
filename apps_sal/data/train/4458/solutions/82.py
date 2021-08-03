def time_correct(t):
    try:
        if not t:
            return t
        if not len(t) == 8:
            return None
        h, m, s = map(int, t.split(':'))
        s, m = s % 60, m + (s - (s % 60)) // 60
        m, h = m % 60, h + (m - (m % 60)) // 60
        h %= 24
        return f'{h:02}:{m:02}:{s:02}'
    except:
        return None
