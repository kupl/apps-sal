import re

def time_correct(t):
    if not t:
        return t
    
    if not re.match('^\d\d:\d\d:\d\d$', t):
        return None
    
    h, m, s = map(int, t.split(':'))
    
    o, s = divmod(s, 60)
    o, m = divmod(m + o, 60)
    o, h = divmod(h + o, 24)
    
    return '%02d:%02d:%02d' % (h, m, s)
