def dropzone(p, d):
    res,ds=[],1000
    for i in range(0,3):
        d0=((p[0]-d[i][0])**2+(p[1]-d[i][1])**2)
        if d0<ds:
            ds=d0
            res=d[i]
    return res

