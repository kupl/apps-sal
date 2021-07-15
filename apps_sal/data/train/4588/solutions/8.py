def controller(events):
    d,m,opening=0,0,True
    r=''
    for e in events:
        if e=='P':
            if m==0:
                if d==0:
                    m=1
                    opening=True
                elif d==5:
                    m=-1
                    opening=False
                elif opening:
                    m=1
                else:
                    m=-1
            else:
                m=0
        elif e=='O':
            opening=not opening
            m*=-1
        d+=m
        if (m==1 and d==5) or (m==-1 and d==0):
            m=0
        r+=str(d)
    return r
