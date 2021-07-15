def oddest(a):
    res = {k: k for k in a}
    if len(a) <2:
        return  -1 if len(a) ==0 else a[0] 
    while len(a)>1:
        if any(i%2 for i in a):
            res = {k:v for k,v in list(res.items()) if v%2}
            a = list(res.values())
        for k, v in list(res.items()):
            res[k] = v//2 if v%2 ==0 else (v-1)//2
        a = list(res.values())
    
    return k

