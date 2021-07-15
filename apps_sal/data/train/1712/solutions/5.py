def puzzle_solver(pieces, width, height):
    l,u,p={},{},{}
    s=[]
    r=[]
    for ((a,b),(c,d),e) in pieces:
        p[e]=(a,b),(c,d)
        l[(a,c)]=e
        u[(a,b)]=e
        if a==b==c==None:r+=[e]
    while 1:
        (a,b),(c,d)=p[r[-1]]
        if b==d==None:
            s+=[tuple(r)]
            r=[]
            if c==None:
                break
            (w,x),(y,z)=p[s[-1][0]]
            r+=[u[(y,z)]]
        else:
            n=l[(b,d)]
            r+=[n]
    return s
