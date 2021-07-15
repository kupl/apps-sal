def LDTA(n):
    x,s = n,set(str(n))
    for _ in range(30):
        x *= n
        for d in str(x):
            s.add(d)
            if len(s)==10: return int(d)
