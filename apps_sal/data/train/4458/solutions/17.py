import re

def time_correct(t):
    if t == '':
        return ''
    
    if t is None or len(t.split(':')) != 3:
        return None
    
    try:
        p = re.compile('^\d{2}$')
        
        h, m, s = [int(n) for n in t.split(':') if p.search(n)]
        
    except:
        return None
    
    if s >= 60: 
        m += (s // 60)
        s = (s - ((s // 60 ) * 60))
    if m >= 60:
        h += (m // 60)
        m = (m - ((m // 60 ) * 60))
    
    if h == 24:
        h = 0
    elif h > 24:
        h = h % 24
        
    return f"{'0' + str(h) if h < 10 else h}:{'0' + str(m) if m < 10 else m}:{'0' + str(s) if s < 10 else s}"

