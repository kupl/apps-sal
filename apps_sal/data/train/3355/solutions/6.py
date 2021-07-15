def spoc(sn, cyfry):
    if sn.endswith(cyfry): return 0
    cp, co = cyfry
    res = 0
    ico = sn.rfind(co)
    res += len(sn) - ico - 1
    sn = sn[:ico] + sn[ico+1:]
    icp = sn.rfind(cp)
    res += len(sn) - icp - 1
    sn = sn[:icp] + sn[icp+1:]
    lpz,i  = 0, 0
    if len(sn) > 0 and len(sn) == sn.count('0'): return None
    while sn and sn[i] == '0':
        i += 1
        lpz += 1
    return res + lpz
    
def solve(n):
    print(n)
    sn, t = str(n), []
    if sn.count('0') > 1:
        t.append(spoc(sn, '00'))
    for p, d in ('25', '50', '75'):
        if p in sn and d in sn:
            x = spoc(sn, p + d)
            if x is not None: t.append(x)
    return min(t) if t else -1

