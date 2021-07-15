def sum_for_list(lst):
    r=[]
    for i in lst:
        r.append(abs(i))
    k=[]
    for i in r:
        l=[]
        for j in range(2,i+1):
            if i%j==0:
                l.append(j)
        
        
        
        for x in l:
            g=[]
            for y in range(1,x+1):
                if x%y==0:
                    g.append(y)
            
            if g[0]==1 and g[1]==x:
                k.append(x)
                
    
    s=set(k)
    
    p=[]
    for i in s:
        o=[i]
        a=0
        for j in lst:
            if j%i==0:
                a=a+j
        o.append(a)
        
        p.append(o)
        
    p.sort()
    return p
