def per(n):
    r = []
    while n>=10:
        p=1
        for i in str(n):
            p=p*int(i)
        r.append(p)
        n = p
    return r
