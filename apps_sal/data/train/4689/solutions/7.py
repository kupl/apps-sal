def create_report(arr):
    d = {}
    for i in arr:
        if 'Labrador Duck' in i: return ['Disqualified data']
        *s,v = i.replace('-',' ').split()
        if len(s) == 4:
            k = s[0][0]+s[1][0]+s[-2][:2]+s[-1][:2]
        elif len(s) == 3:
            k = ''.join(j[:2] for j in s)
        elif len(s) == 2:
            k = ''.join(j[:3] for j in s)
        else:
            k = s[0][:6]
        k = k.upper()
        d.setdefault(k,0)
        d[k] += int(v)
        
    r = []
    for k in sorted(d):
        r.extend([k,d.get(k)])
    
    return r

