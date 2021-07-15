def inverseMod(a, m):
    r1, s1, r2, s2 = a, 1, m, 0
    while r2>0:
        q = r1//r2
        r1, s1, r2, s2 = r2, s2, r1-q*r2, s1-q*s2
    if r1==1:
        return s1%m


