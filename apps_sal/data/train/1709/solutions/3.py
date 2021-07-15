def sum_for_list(lst):
    def buscar_primxs(x):
        res=[]
        x=abs(x)
        for i in range(2,int(x/2)+1):
            if (x//i)*i==x:
                    if i==2 or i==3:
                        res.append(i)
                    else:
                        c=0
                        for j in range(2,i):
                             if (i//j)*j==i:
                                    c=c+1
                        if c==0:
                            res.append(i)
        if res==[]:
            return([x])
        return(res)
        
    R={}
    for x in lst:
        for elements in buscar_primxs(x):
            if elements in R:
                R[elements]+=x
            else:
                R[elements]=x
    rta=[]
    
    M=[x for x in R]

    M=sorted(M)

    for keys in M:
        rta.append([keys,R[keys]])
    return(rta)
