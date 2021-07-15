def time_correct(t):
    try:
        h = t.split(":")[0]
        m = t.split(":")[1]
        s = t.split(":")[2]
        
        if h[0]==0: h = h[1]
        if m[0]==0: m = m[1]
        if s[0]==0: s = s[1]
        
        h = int(h)
        m = int(m)
        s = int(s)
        
        while s > 59:
            m += 1
            s -= 60
        while m > 59:
            h += 1
            m -= 60
        while h > 23:
            h -= 24
        
        h = str(h)
        m = str(m)
        s = str(s)
        
        if len(h)==1: h = "0" + h
        if len(m)==1: m = "0" + m
        if len(s)==1: s = "0" + s
        
        return ":".join([h,m,s])
    except:
        return '' if t=='' else None
