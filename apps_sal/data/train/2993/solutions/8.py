def poly_add(a, b):
    res = []
    if len(b)>len(a):
        a, b = b, a

    for i,n in enumerate(a):
        try:
            res.append(n+b[i])
        except:
            res.append(n)
        
    return res
