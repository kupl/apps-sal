from functools import reduce    

def updateParts(d,s,n,p):
    d.append(p)
    for t in list(s):
        s.add(tuple(sorted(t+(p,))))
        for i in range(len(t)):
            s.add( tuple(sorted(t[:i]+(p*t[i],)+(t[i+1:]))) )
    s.add((p,))
    return n//p

def prod_int_partII(n,m):
    x,d,s,p = n,[],set(),2
    while p*p<=n:
        while not n%p: n = updateParts(d,s,n,p)
        p += 1+(p!=2)
    if n-1 and n!=x: updateParts(d,s,-1,n)
    
    s = [t for t in s if reduce(int.__mul__,t)==x and len(t)>1]
    d = sorted(list(t) for t in s if len(t)==m)
    
    return [len(s),len(d),d[0] if len(d)==1 else d]
