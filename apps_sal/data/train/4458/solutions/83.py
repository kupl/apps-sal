from re import match

def time_correct(t):
    if not t: return t
    if not bool(match(r'\d{2}:\d{2}:\d{2}', t)): return None
    
    h, m, s = map(int, t.split(':'))
    if s > 59: 
        m += s // 60
        s %= 60
    if m > 59: 
        h += m // 60
        m %= 60
    if h > 23:
        h %= 24
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
