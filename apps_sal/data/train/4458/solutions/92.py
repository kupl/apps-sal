def time_correct(t):
    if not t:
        return t
    try:
        h, m, s = map(int, t.split(':'))
    except ValueError:
        return None
    
    m, s = m + s//60, s % 60
    h, m = h + m//60, m % 60
    h = h % 24
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
