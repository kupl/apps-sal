def past(h, m, s):
    if h > 0:
        h = h*60*60*1000
    if m> 0:
        m = m*60*1000
    if s> 0:
        s = s*1000
        
    return h+s+m
